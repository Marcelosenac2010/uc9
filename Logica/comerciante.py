n = int(input("Serao digitados dados de quantos produtos? "))

nomes = ["" for x in range(n)]
precos_compra = [0.0 for x in range(n)]
precos_venda = [0.0 for x in range(n)]

# 1. Leitura dos dados de cada produto
for i in range(n):
    print(f"Produto {i+1}:")
    nomes[i] = input("Nome: ")
    precos_compra[i] = float(input("Preco de compra: "))
    precos_venda[i] = float(input("Preco de venda: "))

abaixo_10 = 0
entre_10_20 = 0
acima_20 = 0
total_compra = 0.0
total_venda = 0.0

# 2. Processamento de cada mercadoria
for i in range(n):
    lucro = precos_venda[i] - precos_compra[i]
    percentual_lucro = (lucro / precos_compra[i]) * 100

    # Categorização pelas faixas de lucro
    if percentual_lucro < 10.0:
        abaixo_10 += 1
    elif percentual_lucro <= 20.0:
        entre_10_20 += 1
    else:
        acima_20 += 1

    # Acumulação dos totais
    total_compra += precos_compra[i]
    total_venda += precos_venda[i]

total_lucro = total_venda - total_compra

# 3. Exibição do relatório final
print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo_10}")
print(f"Lucro entre 10% e 20%: {entre_10_20}")
print(f"Lucro acima de 20%: {acima_20}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {total_lucro:.2f}")