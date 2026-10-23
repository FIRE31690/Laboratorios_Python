import operaciones

# Error original:
#     import operaciones
#     print(calcular_subtotal(10000, 3))   # NameError
#
# `import operaciones` solo trae el nombre del módulo, no sus funciones.
# Hay dos formas de corregirlo (sin copiar la función aquí):

# Opción 1: llamar a la función a través del módulo.
print(operaciones.calcular_subtotal(10000, 3))

# Opción 2: importar la función directamente.
from operaciones import calcular_subtotal
print(calcular_subtotal(10000, 3))
