# Ejercicio — Encabezado y despedida
# El encabezado se define una sola vez y se llama dos veces.

def mostrar_encabezado():
    print("==========================")
    print("     INVENTARIO PYTHON")
    print("==========================")


def mostrar_despedida():
    print("--------------------------")
    print("  Gracias por usar el programa")
    print("--------------------------")


mostrar_encabezado()
print("Registro de productos")
mostrar_encabezado()
print("Consulta de productos")
mostrar_despedida()
