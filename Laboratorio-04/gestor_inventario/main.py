import math

from almacenamiento import cargar_inventario, guardar_inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv


MENU = "\n".join((
    "",
    "================================",
    "       GESTOR DE INVENTARIO",
    "================================",
    "1. Registrar producto",
    "2. Listar productos",
    "3. Buscar por código",
    "4. Actualizar existencias",
    "5. Eliminar producto",
    "6. Consultar productos sin stock",
    "7. Resumen del inventario",
    "8. Guardar inventario",
    "9. Exportar reporte CSV",
    "0. Salir",
))


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Escribe un número entero válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"El valor debe ser al menos {minimo}.")
            continue
        return valor


def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Escribe un precio numérico.")
            continue
        if not math.isfinite(precio) or precio <= 0:
            print("El precio debe ser positivo y finito.")
            continue
        return precio


def presentar_producto(producto):
    print(
        f"{producto.codigo} | {producto.nombre} | {producto.categoria} | "
        f"${producto.precio:.2f} | existencias: {producto.cantidad}"
    )


def guardar_y_confirmar(inventario):
    try:
        ruta = guardar_inventario(inventario)
    except OSError as error:
        print(f"No se confirmó el guardado: {error}")
    else:
        print(f"Inventario guardado: {ruta}")


def registrar_producto(inventario):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    print("Categorías:", ", ".join(CATEGORIAS))
    categoria = input("Categoría: ").strip()
    precio = leer_precio("Precio: ")
    cantidad = leer_entero("Cantidad: ", minimo=0)
    inventario.registrar(Producto(codigo, nombre, categoria, precio, cantidad))
    print("Producto registrado.")
    guardar_y_confirmar(inventario)


def ejecutar():
    try:
        inventario = cargar_inventario()
    except (OSError, ValueError) as error:
        print(f"No se pudo cargar el inventario: {error}")
        print("El archivo original no se modificó. Corrige o restaura el JSON antes de continuar.")
        return

    print(f"Datos cargados: {len(inventario.listar())} producto(s).")
    while True:
        print(MENU)
        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                registrar_producto(inventario)
            elif opcion == "2":
                productos = inventario.listar()
                if not productos:
                    print("El inventario está vacío.")
                for producto in productos:
                    presentar_producto(producto)
            elif opcion == "3":
                producto = inventario.buscar(input("Código: ").strip())
                if producto is None:
                    print("No se encontró el producto.")
                else:
                    presentar_producto(producto)
            elif opcion == "4":
                codigo = input("Código: ").strip()
                cantidad = leer_entero("Nueva cantidad: ", minimo=0)
                inventario.actualizar_existencias(codigo, cantidad)
                print("Existencias actualizadas.")
                guardar_y_confirmar(inventario)
            elif opcion == "5":
                inventario.eliminar(input("Código: ").strip())
                print("Producto eliminado.")
                guardar_y_confirmar(inventario)
            elif opcion == "6":
                agotados = inventario.sin_stock()
                if not agotados:
                    print("No hay productos sin stock.")
                for producto in agotados:
                    presentar_producto(producto)
            elif opcion == "7":
                resumen = inventario.resumen()
                print(f"Productos registrados: {resumen['productos']}")
                print(f"Unidades disponibles: {resumen['unidades']}")
                print(f"Valor total: ${resumen['valor']:.2f}")
                print(f"Categorías utilizadas: {resumen['categorias']}")
            elif opcion == "8":
                guardar_y_confirmar(inventario)
            elif opcion == "9":
                print(f"Reporte exportado: {exportar_csv(inventario)}")
            elif opcion == "0":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida.")
        except (KeyError, TypeError, ValueError) as error:
            print(f"Operación rechazada: {error}")
        except OSError as error:
            print(f"No se pudo completar la operación de archivo: {error}")


if __name__ == "__main__":
    ejecutar()