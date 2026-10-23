# Ejercicio — Reintentar una cantidad

while True:
    texto = input("Cantidad: ")

    try:
        cantidad = int(texto)
    except ValueError:
        print("Debes escribir un entero.\n")
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.\n")
        continue

    print("Cantidad aceptada:", cantidad)
    break
