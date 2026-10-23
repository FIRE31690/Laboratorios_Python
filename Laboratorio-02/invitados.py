invitados = []
for posicion in range(1, 6):
    invitados.append(input(f"Nombre del invitado {posicion}: ").strip())
print("Cantidad:", len(invitados))
print("Invitados:", invitados)
