import json
from pathlib import Path

from inventario import Inventario
from producto import Producto


BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


def guardar_inventario(inventario):
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    ruta_temporal = RUTA_JSON.with_suffix(".json.tmp")
    try:
        with ruta_temporal.open("w", encoding="utf-8") as archivo:
            json.dump(inventario.exportar_datos(), archivo, ensure_ascii=False, indent=4)
            archivo.write("\n")
        ruta_temporal.replace(RUTA_JSON)
    except OSError:
        ruta_temporal.unlink(missing_ok=True)
        raise
    return RUTA_JSON


def cargar_inventario():
    if not RUTA_JSON.exists():
        return Inventario()

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON inválido en línea {error.lineno}, columna {error.colno}.") from error

    if not isinstance(datos, list):
        raise ValueError("La raíz del archivo JSON debe ser una lista.")

    temporal = Inventario()
    for indice, registro in enumerate(datos, start=1):
        try:
            temporal.registrar(Producto.desde_diccionario(registro))
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Registro {indice} inválido: {error}") from error
    return temporal