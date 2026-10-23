# Depuración — Lista compartida
# Error original: `productos = []` estaba en el cuerpo de la clase, así que
# todos los inventarios compartían la misma lista.
# Corrección: crear la lista dentro de __init__ (una por objeto).

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print(segundo.productos)  # []
