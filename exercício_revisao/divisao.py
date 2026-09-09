n = int(input("Quantas contas você deseja fazer: \n"))

for i in range(n):
    num = int(input("Qual o numerador: \n"))
    den = int(input("Qual o divisor: \n"))

    if den == 0:
        print("Divisão por zero não existe!\n")
    else:
        div = num / den
        print(f"Resultado da divisão: {div:.2f}\n")