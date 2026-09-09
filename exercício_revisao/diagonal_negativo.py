n = int(input("Qual a ordem da matriz? "))

mat = []
for i in range(n):
    linha = []
    for j in range(n):
        val = int(input(f"Elemento [{i},{j}]: "))
        linha.append(val)
    mat.append(linha)

print("DIAGONAL PRINCIPAL:")
for i in range(n):
    print(mat[i][i], end=" ")
print()

negativos = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            negativos += 1

print(f"QUANTIDADE DE NEGATIVOS = {negativos}")