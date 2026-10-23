# Reto — Billetera orientada a objetos

class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self._saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self._saldo:
            return False
        self._saldo -= monto
        return True

    def consultar_saldo(self):
        return self._saldo


ana = Billetera("Ana")
luis = Billetera("Luis")

print("Ana ingresa 100000:", ana.registrar_ingreso(100000))  # True
print("Ana gasta 30000:", ana.registrar_gasto(30000))        # True
print("Ana gasta 500000:", ana.registrar_gasto(500000))      # False (excede saldo)
print("Ana ingresa -50:", ana.registrar_ingreso(-50))        # False (monto no positivo)

print("Luis ingresa 20000:", luis.registrar_ingreso(20000))  # True
print("Luis gasta 0:", luis.registrar_gasto(0))              # False

print(f"Saldo de {ana.titular}: {ana.consultar_saldo()}")    # 70000
print(f"Saldo de {luis.titular}: {luis.consultar_saldo()}")  # 20000
