import unidades

km = float(input("Kilómetros: "))
print(f"{km} km = {unidades.kilometros_a_metros(km)} m")

celsius = float(input("Grados Celsius: "))
print(f"{celsius} °C = {unidades.celsius_a_fahrenheit(celsius)} °F")
