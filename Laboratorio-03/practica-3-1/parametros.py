# Sección 2 — Parámetros y argumentos

def saludar(nombre):
    print(f"Hola, {nombre}")


saludar("Laura")
saludar("Andrés")


def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")


mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)


# Antes de ejecutar — Predice
def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


presentar("Ana", "Bogotá")

# Predicción: NO hay error. Python asigna los argumentos por posición,
# así que la llamada original presentar("Cali", "Luis") imprimiría
# "Cali vive en Luis" (una frase extraña, pero válida).
# Corrección: respetar el orden nombre, ciudad.
presentar("Luis", "Cali")
