materias = ["Python", "Matemáticas", "Bases de datos"]
for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)
materias.append("Inglés")
print("Después de agregar:")
for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)
