tareas = []
opcion = ""
while opcion != "0":
    print("\n1. Agregar tarea\n2. Mostrar tareas\n3. Consultar cantidad\n0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        tarea = input("Tarea: ").strip()
        if tarea:
            tareas.append(tarea)
    elif opcion == "2":
        if tareas:
            for posicion, tarea in enumerate(tareas, start=1):
                print(posicion, "-", tarea)
        else:
            print("No hay tareas.")
    elif opcion == "3":
        print("Cantidad:", len(tareas))
    elif opcion != "0":
        print("Opción no válida.")
