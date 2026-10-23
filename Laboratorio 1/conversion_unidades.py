nombre = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas: "))
valor_hora = float(input("Valor por hora: "))

pago_total = horas * valor_hora

print("-------------------------")
print("RESUMEN DE PAGO")
print("-------------------------")
print("Trabajador:", nombre)
print("Horas:", horas)
print("Valor por hora: $", valor_hora)
print("Pago total: $", pago_total)
