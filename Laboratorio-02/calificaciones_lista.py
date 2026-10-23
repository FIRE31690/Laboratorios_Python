calificaciones = [4.5, 3.2, 2.8, 5.0, 3.2, 4.0]
print("Primeras tres:", calificaciones[:3])
print("Últimas dos:", calificaciones[-2:])
print("Cantidad:", len(calificaciones))
print("Ordenadas:", sorted(calificaciones))
nota = float(input("Nota para contar: "))
print("Repeticiones:", calificaciones.count(nota))
