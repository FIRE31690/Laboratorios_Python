# Comprobación no interactiva de categoria_valida()
from validaciones import categoria_valida, CATEGORIAS

print(categoria_valida("Periféricos", CATEGORIAS))  # True
print(categoria_valida("Juguetes", CATEGORIAS))     # False
