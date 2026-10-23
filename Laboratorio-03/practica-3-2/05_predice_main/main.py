from mensajes import despedir

print(despedir())

# Predicción:
#   python main.py     -> Hasta luego
#                         (al importar, __name__ vale "mensajes", así que
#                          el bloque "Prueba directa" NO se ejecuta)
#   python mensajes.py -> Prueba directa
#                         (al ejecutarlo directo, __name__ vale "__main__";
#                          despedir() se define pero nadie la llama)
