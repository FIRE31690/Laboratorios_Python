opcion = ""
while opcion != "0":
    print("\n1. Saludar\n2. Mostrar mensaje\n0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        print("Hola.")
    elif opcion == "2":
        print("El programa sigue ejecutándose.")
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
