# Sección 7 — Atributo de clase y atributo de instancia

# Versión con error: la lista vive en la CLASE y se comparte.
class RegistroCompartido:
    elementos = []


primero = RegistroCompartido()
segundo = RegistroCompartido()

primero.elementos.append("Teclado")
print("Compartido ->", segundo.elementos)  # ['Teclado'] (¡no debería!)


# Versión corregida: cada objeto crea su propia lista en __init__.
class Registro:
    def __init__(self):
        self.elementos = []


primero = Registro()
segundo = Registro()

primero.elementos.append("Teclado")

print("Primero:", primero.elementos)  # ['Teclado']
print("Segundo:", segundo.elementos)  # []
