from producto import Producto


class Inventario:
    def __init__(self):
        self._productos = {}

    def registrar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden registrar objetos Producto.")
        if producto.codigo in self._productos:
            raise ValueError("Ya existe un producto con ese código.")
        self._productos[producto.codigo] = producto

    def listar(self):
        return tuple(self._productos.values())

    def buscar(self, codigo):
        return self._productos.get(codigo)

    def actualizar_existencias(self, codigo, cantidad):
        producto = self._productos.get(codigo)
        if producto is None:
            raise KeyError("No existe un producto con ese código.")
        producto.actualizar_cantidad(cantidad)

    def eliminar(self, codigo):
        if codigo not in self._productos:
            raise KeyError("No existe un producto con ese código.")
        del self._productos[codigo]

    def sin_stock(self):
        return tuple(producto for producto in self._productos.values() if producto.cantidad == 0)

    def exportar_datos(self):
        return [producto.a_diccionario() for producto in self._productos.values()]

    def resumen(self):
        productos = self.listar()
        return {
            "productos": len(productos),
            "unidades": sum(producto.cantidad for producto in productos),
            "valor": sum(producto.precio * producto.cantidad for producto in productos),
            "categorias": len({producto.categoria for producto in productos}),
        }