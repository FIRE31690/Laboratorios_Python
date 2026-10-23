import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"
CAMPOS = ("codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario")


def exportar_csv(inventario):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)
    filas = []
    for datos in inventario.exportar_datos():
        fila = dict(datos)
        fila["valor_inventario"] = datos["precio"] * datos["cantidad"]
        filas.append(fila)

    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)
    return RUTA_CSV