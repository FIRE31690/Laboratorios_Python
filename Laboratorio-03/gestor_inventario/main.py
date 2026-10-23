"""Interfaz de consola del gestor de inventario.

Responsabilidades de este archivo: pedir datos, mostrar el menú y
presentar los resultados. La lógica vive en Producto e Inventario.
"""

# Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# main:
#   solicita datos
#   muestra menú
#   informa los resultados

import math

from producto import CATEGORIAS, Producto
from inventario import Inventario


def mostrar_menu():
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")


# ---------- Lectura de datos ----------
def leer_texto(mensaje):
    return input(mensaje).strip()


def leer_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(mensaje))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def leer_precio(mensaje="Precio: "):
    while True:
        try:
            precio = float(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if not math.isfinite(precio) or precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


# ---------- Presentación ----------
def formatear_producto(producto):
    return (
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} - "
        f"${producto.precio} - {producto.cantidad} unidades"
    )


# ---------- Opciones del menú ----------
def registrar(inventario):
    codigo = leer_texto("Código: ")

    if codigo and inventario.buscar_por_codigo(codigo) is not None:
        print("Registro rechazado: ya existe un producto con ese código.")
        return

    nombre = leer_texto("Nombre: ")
    print("Categorías permitidas:", ", ".join(CATEGORIAS))
    categoria = leer_texto("Categoría: ")
    precio = leer_precio()
    cantidad = leer_cantidad()

    # El producto solo se construye cuando ya están todos los datos:
    # si algo es inválido no queda ningún registro parcial.
    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print(f"Registro rechazado: {error}")
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print("Registro rechazado: ya existe un producto con ese código.")


def listar(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("El inventario está vacío.")
        return

    for producto in productos:
        print(formatear_producto(producto))


def buscar(inventario):
    codigo = leer_texto("Código: ")
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print("Producto no registrado.")
    else:
        print(formatear_producto(producto))


def actualizar(inventario):
    codigo = leer_texto("Código: ")

    if inventario.buscar_por_codigo(codigo) is None:
        print("Producto no registrado.")
        return

    nueva_cantidad = leer_cantidad("Nueva cantidad: ")

    if inventario.actualizar_existencias(codigo, nueva_cantidad):
        print("Existencias actualizadas.")
    else:
        print("Actualización rechazada.")


def eliminar(inventario):
    codigo = leer_texto("Código: ")

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print("Producto no registrado.")


def mostrar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("No hay productos sin existencias.")
        return

    print("Sin existencias:")
    for nombre in agotados:
        print(f"- {nombre}")


def mostrar_resumen(inventario):
    datos = inventario.resumen()
    categorias = ", ".join(datos["categorias"]) or "ninguna"

    print(f"Productos registrados: {datos['productos']}")
    print(f"Unidades disponibles: {datos['unidades']}")
    print(f"Valor del inventario: ${datos['valor']}")
    print(f"Categorías utilizadas: {categorias}")


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            actualizar(inventario)
        elif opcion == "5":
            eliminar(inventario)
        elif opcion == "6":
            mostrar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
