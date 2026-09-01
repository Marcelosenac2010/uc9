m = int(input("digite um valor (M): "))
n = int(input("digite um valor (N): "))

mat = []
for i in range(n):
    linha = []
    for j in range(n):
        val = int(input(f"Elemento [{i},{j}]: "))
        linha.append(val)
    mat.append(linha)

print()