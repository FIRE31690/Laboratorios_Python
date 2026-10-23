depositos = 0
total = 0
while True:
    valor = float(input("Depósito (0 para terminar): "))
    if valor == 0:
        break
    if valor < 0:
        print("El depósito debe ser positivo.")
        continue
    total += valor
    depositos += 1
    print("Ahorro acumulado:", total)
print("Depósitos válidos:", depositos)
print("Total ahorrado:", total)
