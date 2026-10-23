# Sección 6 — Alcance de las variables

def duplicar(numero):
    resultado = numero * 2
    return resultado


doble = duplicar(8)
print(doble)

# `resultado` es una variable LOCAL de duplicar(): deja de existir cuando
# la función termina. Fuera de ella solo tenemos el valor devuelto (doble).
try:
    print(resultado)
except NameError as error:
    print("Error esperado:", error)
