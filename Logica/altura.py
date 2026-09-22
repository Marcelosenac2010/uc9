n = int(input("Quantas pessoas serao digitadas? "))

nomes = [""] * n
idades = [0] * n
alturas = [0.0] * n

for i in range(n):
    print(f"Dados da {i + 1}a pessoa:")
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idade: "))
    alturas[i] = float(input("Altura: "))

soma_alturas = 0.0
menores_16 = 0

for i in range(n):
    soma_alturas += alturas[i]
    if idades[i] < 16:
        menores_16 += 1

media_altura = soma_alturas / n if n > 0 else 0.0
porcentagem_menores = (menores_16 / n) * 100 if n > 0 else 0.0

print(f"\nAltura média: {media_altura:.2f}")
print(f"Pessoas com menos de 16 anos: {porcentagem_menores:.1f}%")

for i in range(n):
    if idades[i] < 16:
        print(nomes[i])