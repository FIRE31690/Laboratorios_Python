# Sección 7 — Funciones y listas

def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))  # 11


# Modifica la lista recibida (la lista original cambia)
def agregar(nombre, nombres):
    nombres.append(nombre)


productos = ["Teclado"]
agregar("Mouse", productos)
print(productos)  # ['Teclado', 'Mouse']


# Devuelve una lista nueva (la original no cambia)
def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)
