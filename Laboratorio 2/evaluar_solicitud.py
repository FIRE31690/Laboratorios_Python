edad = int(input("Edad: "))
inscrito = input("¿Está inscrito? (si/no): ").strip().lower() == "si"
documentos = int(input("Documentos entregados: "))
cumple = True
if edad < 16:
    print("Falta cumplir la edad mínima.")
    cumple = False
if not inscrito:
    print("La persona no está inscrita.")
    cumple = False
if documentos < 3:
    print("Faltan documentos.")
    cumple = False
print("Solicitud aprobada." if cumple else "Solicitud no aprobada.")
