import csv
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import almacenamiento
import main
import reportes
from inventario import Inventario
from producto import Producto


class PruebasInventario(unittest.TestCase):
    def crear_producto(self, codigo="P001", nombre="Teclado", categoria="Periféricos", precio=85000, cantidad=4):
        return Producto(codigo, nombre, categoria, precio, cantidad)

    def test_rechaza_precio_no_finito_y_cantidad_negativa(self):
        for precio in (float("nan"), float("inf"), -1, 0):
            with self.subTest(precio=precio), self.assertRaises(ValueError):
                self.crear_producto(precio=precio)
        with self.assertRaises(ValueError):
            self.crear_producto(cantidad=-1)

    def test_rechaza_codigo_duplicado(self):
        inventario = Inventario()
        inventario.registrar(self.crear_producto())
        with self.assertRaises(ValueError):
            inventario.registrar(self.crear_producto(nombre="Otro"))

    def test_archivo_danado_intacto_y_carga_sin_parciales(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "productos.json"
            ruta.write_text("[\n", encoding="utf-8")
            with patch.object(almacenamiento, "RUTA_JSON", ruta):
                with self.assertRaises(ValueError):
                    almacenamiento.cargar_inventario()
            self.assertEqual(ruta.read_text(encoding="utf-8"), "[\n")

            registros = [self.crear_producto().a_diccionario(), self.crear_producto(nombre="Duplicado").a_diccionario()]
            ruta.write_text(json.dumps(registros), encoding="utf-8")
            with patch.object(almacenamiento, "RUTA_JSON", ruta):
                with self.assertRaisesRegex(ValueError, "código"):
                    almacenamiento.cargar_inventario()

    def test_persistencia_totales_y_csv(self):
        inventario = Inventario()
        inventario.registrar(self.crear_producto())
        inventario.registrar(self.crear_producto("P002", "Mouse", "Periféricos", 45000, 0))
        inventario.registrar(self.crear_producto("P003", "Monitor", "Componentes", 700000, 2))
        self.assertEqual(inventario.resumen(), {"productos": 3, "unidades": 6, "valor": 1740000.0, "categorias": 2})

        with tempfile.TemporaryDirectory() as temporal:
            ruta_json = Path(temporal) / "datos" / "productos.json"
            ruta_csv = Path(temporal) / "reportes" / "inventario.csv"
            with patch.object(almacenamiento, "RUTA_JSON", ruta_json), patch.object(reportes, "RUTA_CSV", ruta_csv):
                almacenamiento.guardar_inventario(inventario)
                recuperado = almacenamiento.cargar_inventario()
                self.assertEqual(recuperado.exportar_datos(), inventario.exportar_datos())
                recuperado.actualizar_existencias("P002", 5)
                self.assertEqual(recuperado.resumen()["valor"], 1965000.0)
                reportes.exportar_csv(recuperado)
                with ruta_csv.open(encoding="utf-8", newline="") as archivo:
                    filas = list(csv.DictReader(archivo))
                self.assertEqual(filas[1]["valor_inventario"], "225000.0")

    def test_menu_registra_guarda_y_muestra_resumen(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "datos" / "productos.json"
            entradas = ["1", "P001", "Teclado", "Periféricos", "85000", "4", "7", "0"]
            salida = io.StringIO()
            with patch.object(almacenamiento, "RUTA_JSON", ruta), patch("builtins.input", side_effect=entradas):
                with redirect_stdout(salida):
                    main.ejecutar()

            datos = json.loads(ruta.read_text(encoding="utf-8"))
            self.assertEqual(datos[0]["codigo"], "P001")
            self.assertIn("Valor total: $340000.00", salida.getvalue())


if __name__ == "__main__":
    unittest.main()