numeros = [3, 8, 12, 5, 20, 7]
print([numero for numero in numeros if numero >= 10])
notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]
print("Aprobadas:", [nota for nota in notas if nota >= 3.0])
print("Inferiores:", [nota for nota in notas if nota < 3.0])
print("Duplicadas:", [nota * 2 for nota in notas])
