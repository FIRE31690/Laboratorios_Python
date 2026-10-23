producto = {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4}
precio = float(input("Nuevo precio: "))
if precio > 0:
    producto["precio"] = precio
else:
    print("El precio debe ser mayor que cero.")
for clave, valor in producto.items():
    print(clave, ":", valor)
