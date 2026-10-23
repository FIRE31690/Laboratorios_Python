CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")
productos = []
opcion = ""

while opcion != "0":
    print("\n================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        codigos = {p["codigo"] for p in productos}
        if not codigo or not nombre:
            print("Código y nombre no pueden estar vacíos.")
        elif codigo in codigos:
            print("El código ya existe.")
        elif categoria not in CATEGORIAS:
            print("Categoría no válida.")
        elif precio <= 0:
            print("El precio debe ser mayor que cero.")
        elif cantidad < 0:
            print("La cantidad no puede ser negativa.")
        else:
            productos.append({"codigo": codigo, "nombre": nombre, "categoria": categoria,
                              "precio": precio, "cantidad": cantidad})
            print("Producto registrado.")
    elif opcion == "2":
        if not productos:
            print("No hay productos registrados.")
        for p in productos:
            print(f'{p["codigo"]} - {p["nombre"]} - {p["categoria"]} - ${p["precio"]} - {p["cantidad"]} unidades')
    elif opcion == "3":
        codigo = input("Código: ").strip()
        encontrado = next((p for p in productos if p["codigo"] == codigo), None)
        print(encontrado if encontrado is not None else "Producto no existe.")
    elif opcion == "4":
        codigo = input("Código: ").strip()
        encontrado = next((p for p in productos if p["codigo"] == codigo), None)
        if encontrado is None:
            print("Producto no existe.")
        else:
            cantidad = int(input("Nueva cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                encontrado["cantidad"] = cantidad
                print("Existencias actualizadas.")
    elif opcion == "5":
        codigo = input("Código: ").strip()
        encontrado = next((p for p in productos if p["codigo"] == codigo), None)
        if encontrado is None:
            print("Producto no existe.")
        else:
            productos.remove(encontrado)
            print("Producto eliminado.")
    elif opcion == "6":
        agotados = [p["nombre"] for p in productos if p["cantidad"] == 0]
        if agotados:
            print("Sin existencias:")
            for nombre in agotados:
                print("-", nombre)
        else:
            print("No hay productos sin stock.")
    elif opcion == "7":
        categorias = {p["categoria"] for p in productos}
        print("Productos:", len(productos))
        print("Unidades:", sum(p["cantidad"] for p in productos))
        print("Valor del inventario:", sum(p["precio"] * p["cantidad"] for p in productos))
        print("Categorías utilizadas:", ", ".join(sorted(categorias)) or "Ninguna")
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
