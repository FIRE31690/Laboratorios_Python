edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()
if edad >= 18 or (edad < 18 and autorizacion == "si"):
    print("Puede ingresar.")
else:
    print("No puede ingresar.")
