libros = [
    {"codigo": "L001", "titulo": "Python básico", "autor": "A. Pérez", "anio": 2022},
    {"codigo": "L002", "titulo": "Datos y listas", "autor": "B. Gómez", "anio": 2023},
    {"codigo": "L003", "titulo": "Programación práctica", "autor": "C. Ruiz", "anio": 2024},
]
codigo = input("Código del libro: ").strip()
encontrado = next((libro for libro in libros if libro["codigo"] == codigo), None)
print(encontrado if encontrado is not None else "Libro no localizado.")
