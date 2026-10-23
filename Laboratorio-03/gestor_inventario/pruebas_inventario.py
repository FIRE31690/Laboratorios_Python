"""Pruebas obligatorias (sección 16) y comprobación numérica (sección 17).

Ejecuta:  python pruebas_inventario.py
"""

from inventario import Inventario
from producto import Producto


def crear(codigo="P001", nombre="Teclado", categoria="Periféricos",
          precio=85000, cantidad=4):
    return Producto(codigo, nombre, categoria, precio, cantidad)


def debe_fallar(**datos):
    try:
        crear(**datos)
    except ValueError:
        return True
    return False


def probar():
    inv = Inventario()

    # Inventario vacío
    assert inv.listar_productos() == []
    r = inv.resumen()
    assert (r["productos"], r["unidades"], r["valor"], r["categorias"]) == (0, 0, 0.0, [])

    # Registro y duplicados
    assert inv.registrar_producto(crear()) is True
    assert inv.registrar_producto(crear()) is False

    # Datos inválidos
    assert debe_fallar(codigo="")
    assert debe_fallar(codigo="   ")
    assert debe_fallar(nombre="")
    assert debe_fallar(nombre="  ")
    assert debe_fallar(categoria="Juguetes")
    assert debe_fallar(precio=0)
    assert debe_fallar(precio=-10)
    assert debe_fallar(cantidad=-1)

    # Cantidad cero es válida
    assert crear(codigo="PX", cantidad=0).cantidad == 0

    # Buscar
    assert inv.buscar_por_codigo("P001").nombre == "Teclado"
    assert inv.buscar_por_codigo("P999") is None

    # Actualizar
    assert inv.actualizar_existencias("P001", 10) is True
    assert inv.buscar_por_codigo("P001").cantidad == 10
    assert inv.actualizar_existencias("P001", -3) is False
    assert inv.buscar_por_codigo("P001").cantidad == 10  # se conserva
    assert inv.actualizar_existencias("P999", 1) is False

    # Eliminar
    assert inv.eliminar_producto("P001") is True
    assert inv.eliminar_producto("P999") is False

    # El código no puede reasignarse
    p = crear()
    try:
        p.codigo = "P999"
    except AttributeError:
        pass
    else:
        raise AssertionError("El código no debería poder cambiarse")

    # Comprobación numérica (sección 17)
    inv = Inventario()
    inv.registrar_producto(crear("P001", "Teclado", "Periféricos", 85000, 4))
    inv.registrar_producto(crear("P002", "Mouse", "Periféricos", 45000, 0))
    inv.registrar_producto(crear("P003", "Monitor", "Componentes", 700000, 2))

    r = inv.resumen()
    assert r["productos"] == 3
    assert r["unidades"] == 6
    assert r["valor"] == 1740000.0
    assert len(r["categorias"]) == 2
    assert inv.productos_sin_stock() == ["Mouse"]

    assert inv.actualizar_existencias("P002", 5) is True
    r = inv.resumen()
    assert (r["productos"], r["unidades"], r["valor"]) == (3, 11, 1965000.0)

    # Independencia entre inventarios
    a, b = Inventario(), Inventario()
    a.registrar_producto(crear())
    assert len(a.listar_productos()) == 1
    assert len(b.listar_productos()) == 0

    # La lista devuelta es una copia
    a.listar_productos().clear()
    assert len(a.listar_productos()) == 1

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    probar()
