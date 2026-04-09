class forma():
    def area():
        area = 0
    
class quadrado(forma):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        area = self.lado * self.lado
        return area

quadrado.lado = int(input("Digite o valor do lado do quadrado: "))
quadradoQualquer = quadrado(quadrado.lado)
print(f"A área do quadrado é: {quadradoQualquer.area()}")