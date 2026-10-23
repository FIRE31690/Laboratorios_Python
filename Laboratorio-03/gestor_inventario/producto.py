"""Clase Producto: datos de un artículo y control de sus propias reglas."""

import math

# Única fuente de verdad de las categorías autorizadas.
CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        # Las validaciones se aplican desde la creación del objeto:
        # un producto no puede "nacer" con datos inválidos.
        self._codigo = self._validar_texto(codigo, "código")
        self._nombre = self._validar_texto(nombre, "nombre")
        self._categoria = self._validar_categoria(categoria)
        self._precio = self._validar_precio(precio)
        self._cantidad = self._validar_cantidad(cantidad)

    # ---------- Validaciones internas ----------
    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError(f"El {campo} no puede estar vacío.")
        return valor.strip()

    @staticmethod
    def _validar_categoria(categoria):
        if isinstance(categoria, str):
            categoria = categoria.strip()

        if categoria not in CATEGORIAS:
            permitidas = ", ".join(CATEGORIAS)
            raise ValueError(f"Categoría no permitida. Opciones: {permitidas}.")
        return categoria

    @staticmethod
    def _validar_precio(precio):
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número.")
        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return float(precio)

    @staticmethod
    def _validar_cantidad(cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return cantidad

    # ---------- Propiedades de consulta (el código no tiene setter) ----------
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

    # ---------- Comportamiento ----------
    def actualizar_existencias(self, nueva_cantidad):
        """Cambia solo las existencias. Devuelve True si se aceptó."""
        try:
            self._cantidad = self._validar_cantidad(nueva_cantidad)
        except ValueError:
            return False  # el dato anterior se conserva
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad
