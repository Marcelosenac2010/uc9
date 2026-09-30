class Pai:
    def __init__(self, valor):
        self.valor = valor

    def mostrar_valor(self):
        print(f"O valor do pai é {self.valor}")


class Filho(Pai):
    def __init__(self, valor):
        super().__init__(valor * 2)

    def mostrar_valor(self):
        print(f"O valor do filho é {self.valor}")

pai_obj = Pai(50)
filho_obj = Filho(50) 

print("Digite 1 - se quer ver o pai, 2 - para ver o filho, 3 - se quer terminar")

while True:
    try:
        x = int(input("Digite um valor: "))

        if x == 1:
            pai_obj.mostrar_valor()
        elif x == 2:
            filho_obj.mostrar_valor()
        elif x == 3:
            print("Encerrando o programa...")
            break  
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")
            
    except ValueError:
        print("Erro: Digite apenas números inteiros válidos!")