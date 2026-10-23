class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        # Nota: aquí aún no se validan los datos iniciales; en el reto
        # integrador (práctica 3.5) sí se hará.
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio


producto = Producto("P001", "Teclado", 85000, 4)
print(producto.calcular_valor())  # 340000

# Propiedades de consulta (sin paréntesis)
print(producto.codigo)
print(producto.nombre)
print(producto.cantidad)

# El código no tiene setter: no se puede reasignar
try:
    producto.codigo = "P999"
except AttributeError as error:
    print("No se puede cambiar el código:", error)

# Actualizar existencias con regla
print(producto.actualizar_existencias(10))  # True
print(producto.cantidad)                    # 10
print(producto.actualizar_existencias(-5))  # False
print(producto.cantidad)                    # 10 (sin cambios)

# Setter del precio
producto.precio = 90000
print(producto.precio)  # 90000

try:
    producto.precio = -1
except ValueError as error:
    print("Precio rechazado:", error)
