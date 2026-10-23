import math


CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código es obligatorio.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if categoria not in CATEGORIAS:
            raise ValueError("La categoría no está permitida.")
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")
        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser positivo y finito.")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_cantidad(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise TypeError("Cada producto debe estar representado por un objeto JSON.")
        campos = {"codigo", "nombre", "categoria", "precio", "cantidad"}
        if set(datos) != campos:
            raise ValueError("El registro debe contener exactamente los cinco campos requeridos.")
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"],
        )