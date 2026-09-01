n = int(input("Quantos valores você deseja digitar: \n"))
vetor_A = [0 for x in range (n)]
vetor_B = [0 for x in range (n)]
vetor_C = [0 for x in range (n)]

print(" Vetor A \n")
for i in range(n):
    vetor_A[i] = int(input("digite o valor: \n"))

print (" Vetor B \n")
for i in range(n):
    vetor_B[i] = int(input("digite o valor: \n"))

for i in range(n):
    vetor_C[i] = vetor_A[i] + vetor_B[i]

print ("Impressão das somas: \n")
for i in range(n):
    print(vetor_C[i])