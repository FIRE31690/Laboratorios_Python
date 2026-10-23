# Ejercicio — Consultas de inventario

# Versión 1: for + append()
def agotados(productos):
    nombres = []

    for producto in productos:
        if producto["cantidad"] == 0:
            nombres.append(producto["nombre"])

    return nombres


# Versión 2: comprensión de lista
def agotados_comprension(productos):
    return [p["nombre"] for p in productos if p["cantidad"] == 0]


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 0},
    {"nombre": "Cable HDMI", "cantidad": 0},
]

print(agotados(inventario))              # ['Mouse', 'Cable HDMI']
print(agotados_comprension(inventario))  # ['Mouse', 'Cable HDMI']
