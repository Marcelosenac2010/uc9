largura = float(input("qual a largura: \n"))
cumprimento = float(input("qual a cumprimento: \n"))
valormetro_q = float(input("qual valor do metro quadrado: \n "))
valor_q = cumprimento * largura
total = valor_q * valormetro_q
print(f"O valor do terreno = R${total:.22f}")