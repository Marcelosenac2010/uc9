import math

class Forma:
    def area(self):
        return 0

class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Uso com polimorfismo
formas = [Forma(), Circulo(3), Quadrado(4)]

for f in formas:
    print(f"{f.area():.2f}")