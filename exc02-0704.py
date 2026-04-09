class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def mostrar_velocidade(self):
        print(f"A velocidade do veículo é: {self.velocidade} km/h")

class Carro(Veiculo):
    def abrir_porta(self):
        print("abriu porta do carro.")

fiat_uno = Carro(120)

fiat_uno.mostrar_velocidade()
fiat_uno.abrir_porta()