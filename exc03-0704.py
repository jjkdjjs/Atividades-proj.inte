class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_bonus(self):
        bonus = self.salario * 0.1
        return bonus

class Gerente(Funcionario):
    def calcular_bonus(self):
        bonus = self.salario * 0.2
        return bonus
    
Iuri = Funcionario("Iuri", 3000)
Marcinho = Gerente("Marcinho", 5000)

print(f"O bônus do funcionário {Iuri.nome} é: R${Iuri.calcular_bonus():.2f}")
print(f"O bônus do gerente {Marcinho.nome} é: R${Marcinho.calcular_bonus():.2f}")