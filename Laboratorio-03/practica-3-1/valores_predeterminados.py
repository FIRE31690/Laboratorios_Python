# Sección 5 — Valores predeterminados y argumentos con nombre

def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


# Predicción: 100000.0, 90000.0 y 80000.0
print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio=50000, cantidad=2, descuento=20))
