class Pessoa:
    # Atributo de classe (escopo compartilhado por todas as instâncias)
    contador = 0

    def __init__(self, nome: str):
        # Atributo de instância (escopo exclusivo de cada objeto)
        self.nome = nome
        # Incrementa o atributo de classe a cada nova instância criada
        Pessoa.contador += 1

# Lista para armazenar as instâncias criadas no loop
lista_pessoas = []

print(f"Contador (escopo de classe) antes de iniciar: {Pessoa.contador}\n")

while True:
    entrada = input("Digite um nome (ou digite 'parar' para encerrar): ").strip()
    
    if entrada.lower() == "parar":
        break
    
    # Criar a instância aqui aciona o __init__ e incrementa o contador automaticamente
    nova_pessoa = Pessoa(entrada)
    lista_pessoas.append(nova_pessoa)
    print(f"-> Objeto criado. Nome: {nova_pessoa.nome} | Contador global: {Pessoa.contador}\n")

if lista_pessoas:
    print("\nAtributos de Instância (nome) armazenados em cada objeto:")
    for pessoa in lista_pessoas:
        print(f"- {pessoa.nome} {Pessoa.contador}ª pessoa")