nombre_trabajador = "Yohan Cuellar"
horas_trabajadas = 40
valor_por_hora = 15.50

APORTE = 0.04

salario_bruto = horas_trabajadas * valor_por_hora
aporte = salario_bruto * APORTE
salario_total = salario_bruto - aporte

print("Nombre del trabajador:", nombre_trabajador)
print("Horas trabajadas:", horas_trabajadas)
print("Valor por hora:", valor_por_hora)
print("Salario bruto:", salario_bruto)
print("Aporte del 4%:", aporte)
print("Salario total:", salario_total)
