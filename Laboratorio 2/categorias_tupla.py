categorias = ("Periféricos", "Componentes", "Accesorios", "Papelería")
for posicion, categoria in enumerate(categorias, start=1):
    print(posicion, "-", categoria)
elegida = input("Categoría: ").strip()
print("Categoría válida." if elegida in categorias else "Categoría no registrada.")
print("Cantidad:", len(categorias))
