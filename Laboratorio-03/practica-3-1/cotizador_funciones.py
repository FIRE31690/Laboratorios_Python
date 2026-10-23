# Ejercicio — Cotizador con funciones

def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje):
    # El porcentaje 10 representa 10 %.
    return subtotal * porcentaje / 100


def calcular_impuesto(base, porcentaje):
    # Impuesto calculado sobre la base recibida.
    return base * porcentaje / 100


def formatear(valor):
    # Muestra 20000 en lugar de 20000.0 cuando el valor es entero.
    return int(valor) if valor == int(valor) else valor


precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base = subtotal - descuento
impuesto = calcular_impuesto(base, porcentaje_impuesto)
total = base + impuesto

print("Subtotal:", formatear(subtotal))
print("Descuento:", formatear(descuento))
print("Base después del descuento:", formatear(base))
print("Impuesto:", formatear(impuesto))
print("Total:", formatear(total))
