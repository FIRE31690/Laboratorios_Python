numeros = [1, 2, 3, 4, 5]
cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)
print(cuadrados)
print([numero ** 2 for numero in numeros])
