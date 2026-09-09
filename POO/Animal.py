class Animal:
    def __init__(self):
        pass
    def comer(self):
        return f"Está comendo  "

class Voador(Animal):
    def __init__(self):
        super().__init__()
    def voar(self):
        return f"Está voando "

class Morcego(Voador):
    def __init__(self):
        super().__init__()
    def detalhes(self):
        return f"{self.voar()}e também {self.comer()}".lower()

meu_morcego = Morcego()
print(meu_morcego.detalhes())