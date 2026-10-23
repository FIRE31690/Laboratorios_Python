cantidad = int(input("Cantidad de notas: "))
if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    suma = 0
    for posicion in range(1, cantidad + 1):
        suma += float(input(f"Nota {posicion}: "))
    print("Promedio:", suma / cantidad)
