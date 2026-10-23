print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = int(input("Descuento (%): "))
impuesto = int(input("Impuesto (%): "))

print()
print("-----------------------------")
print("DATOS DE LA COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Descuento (%):", descuento)
print("Impuesto (%):", impuesto)


subtotal = precio_unitario * cantidad

porcentaje_descuento = descuento / 100
valor_descuento = subtotal * porcentaje_descuento

base = subtotal - valor_descuento

porcentaje_impuesto = impuesto / 100
valor_impuesto = base * porcentaje_impuesto

total = base + valor_impuesto

# Resumen final
print()
print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Base: $", base)
print("Impuesto: $", valor_impuesto)
print("TOTAL: $", total)
