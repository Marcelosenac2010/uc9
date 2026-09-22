n = int(input("Quantos valores você deseja digitar: \n"))
vetor = [0 for x in range (n)]
soma = 0
for i in range(n):
    vetor[i] = int(input("Qual o valor: \n"))

for i in range(n):
    print (vetor[i])

for i in range(n):       
    soma += vetor[i]
    contador += 1

media = soma / n
print(f"Soma total: {soma:.2f}")   
print(f"Media: {media:.2f}")