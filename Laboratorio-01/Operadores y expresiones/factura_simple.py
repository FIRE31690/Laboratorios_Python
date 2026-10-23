nombre_producto = "Cuaderno"
precio_unitario = 15000
cantidad = 3
porcentaje_descuento = 10

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento / 100
total = subtotal - valor_descuento

print("Producto:", nombre_producto)
print("Subtotal:", subtotal)
print("Valor del descuento:", valor_descuento)
print("Total después del descuento:", total)