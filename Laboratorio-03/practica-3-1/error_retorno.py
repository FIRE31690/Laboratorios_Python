# Depuración — Faltó devolver el dato
# Error original: la función calculaba `resultado` pero no lo devolvía,
# por eso `total` valía None.

def sumar(a, b):
    resultado = a + b
    return resultado  # <- línea que faltaba


total = sumar(10, 20)
print(total)  # 30
