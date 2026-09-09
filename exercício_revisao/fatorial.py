n = int(input("Qual valor: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"Fatorial: {fatorial}")