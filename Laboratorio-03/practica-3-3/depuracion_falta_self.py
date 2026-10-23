# Depuración — Falta `self`
# Error original: def mostrar():  ->  TypeError: ... takes 0 positional
# arguments but 1 was given (Python pasa el objeto como primer argumento).

class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):  # <- se agregó self
        print(f"Hola, {self.nombre}")


saludo = Saludo("Ana")
saludo.mostrar()
