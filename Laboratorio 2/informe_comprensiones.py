ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000},
]
mayores = [venta["producto"] for venta in ventas if venta["total"] > 100000]
categorias = {venta["categoria"] for venta in ventas}
por_producto = {venta["producto"]: venta["total"] for venta in ventas}
total = sum(venta["total"] for venta in ventas)
print("Ventas superiores a $100000:", mayores)
print("Categorías:", categorias)
print("Por producto:", por_producto)
print("Total:", total)
