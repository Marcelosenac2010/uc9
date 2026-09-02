soma_produtos = 0.0

for i in range(3):
    n = float(input("Qual o número: "))
    if i == 0:
        soma_produtos += n * 2
    elif i == 1:
        soma_produtos += n * 3
    elif i == 2:
        soma_produtos += n * 5

media_ponderada = soma_produtos / 10.0
print(f"A média ponderada é {media_ponderada:.1f}")