from producto import Producto
from inventario import Inventario

inventario = Inventario()

inventario.agregar(Producto("P001", "Teclado"))
inventario.agregar(Producto("P002", "Mouse"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)

encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

# ---- Reto: inventario con reglas ----
print("\n--- Reto ---")
print("Agregar P003 (válido):", inventario.agregar(Producto("P003", "Monitor")))
print("Agregar P001 repetido:", inventario.agregar(Producto("P001", "Otro")))  # False
print("Eliminar P002 (existe):", inventario.eliminar("P002"))                  # True
print("Eliminar P999 (no existe):", inventario.eliminar("P999"))               # False

print("Quedan:")
for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)
