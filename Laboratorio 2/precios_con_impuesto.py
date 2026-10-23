precios = [10000, 20000, 50000, 80000]
con_for = []
for precio in precios:
    con_for.append(precio * 1.19)
con_comprension = [precio * 1.19 for precio in precios]
print("Con for:", con_for)
print("Con comprensión:", con_comprension)
