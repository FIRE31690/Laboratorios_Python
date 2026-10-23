# Ejercicio — Cuenta de puntos

class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0

    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos

    def sumar(self, cantidad):
        if cantidad <= 0:
            return False
        self._puntos += cantidad
        return True

    def canjear(self, cantidad):
        if cantidad <= 0 or cantidad > self._puntos:
            return False
        self._puntos -= cantidad
        return True


def texto(aceptado):
    return "aceptado" if aceptado else "rechazado"


cuenta = CuentaPuntos("Laura")

print("Sumar: 80    ->", texto(cuenta.sumar(80)))      # aceptado
print("Canjear: 30  ->", texto(cuenta.canjear(30)))    # aceptado
print("Canjear: 100 ->", texto(cuenta.canjear(100)))   # rechazado
print("Total:", cuenta.puntos)                          # 50
