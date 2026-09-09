class Veiculo:
    def __init__(self, marca: str, ano: int):
        self.marca = marca
        self.ano = ano
    def detalhes(self):
        return f"Marca {self.marca}, ano {self.ano}"
class Carro(Veiculo):
    def __init__(self, marca: str, ano: int, porta: int):
        super().__init__(marca, ano)
        self.porta = porta
    def detalhes(self):
        return f"{super().detalhes()}, porta {self.porta}"

Meu_carro = Carro("Chevrolet", 1998, 2)
print(Meu_carro.detalhes())