class Conta():
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

class contaCorrente(Conta):
    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque realizado com sucesso. Saldo atual: {self.saldo}")

conta1 = contaCorrente(1000, 500)
conta1.sacar(1200)