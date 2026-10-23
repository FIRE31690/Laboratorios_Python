compra = float(input("Valor de la compra: "))
if compra >= 200000:
    envio = 0
elif compra >= 100000:
    envio = 10000
else:
    envio = 18000
print("Compra:", compra)
print("Envío:", envio)
print("Total:", compra + envio)
