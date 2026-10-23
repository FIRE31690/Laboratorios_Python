# Depuración — Atributo inexistente
# Error original: print(self.nombree) -> AttributeError (el atributo
# se llama `nombre`, con una sola "e").

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(self.nombre)  # <- corregido


Persona("Laura").mostrar()
