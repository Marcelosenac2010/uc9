     
# 1. Pergunta a quantidade de números que o vetor vai receber
quantidade = int(input("Quantos números você vai digitar? "))

# Inicializa o vetor (lista) vazio
vetor = []

# 2. Preenche o vetor com a quantidade exata usando um 'for'
print(f"\nDigite os {quantidade} números inteiros:")
for i in range(quantidade):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)  # Adiciona cada número no vetor

# 3. Organiza o vetor em ordem crescente
vetor.sort()  # ou: vetor = sorted(vetor)

# 4. Mostra o resultado final ordenado
print("\n=== Resultado ===")
print("Vetor organizado em ordem crescente:")
print(vetor)