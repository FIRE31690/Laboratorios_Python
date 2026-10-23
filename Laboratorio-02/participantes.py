grupo_a = ["Ana", "Carlos", "Laura", "Ana"]
grupo_b = ["Laura", "David", "Carlos", "Pablo"]
participantes = set(grupo_a) | set(grupo_b)
print("Personas diferentes:", len(participantes))
participantes.add("Sofía")
participantes.discard("Pablo")
print(participantes)
