"""Clase Inventario: colección de objetos Producto y sus operaciones."""

from producto import Producto


class Inventario:
    def __init__(self):
        # Lista propia de cada instancia (nunca a nivel de clase).
        self._productos = []

    def registrar_producto(self, producto):
        """Registra el producto. False si no es un Producto o el código existe."""
        if not isinstance(producto, Producto):
            return False

        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self):
        # Copia: quien llama no puede alterar la lista interna.
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        if not isinstance(codigo, str):
            return None

        codigo = codigo.strip()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [
            producto.nombre
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        categorias = {producto.categoria for producto in self._productos}

        return {
            "productos": len(self._productos),
            "unidades": sum(p.cantidad for p in self._productos),
            "valor": sum((p.calcular_valor() for p in self._productos), 0.0),
            "categorias": sorted(categorias),
        }
