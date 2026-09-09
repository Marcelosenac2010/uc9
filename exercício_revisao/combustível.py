alcool_qtd = 0
diesel_qtd = 0
gasolina_qtd = 0

while True:
    try:
        N = int(input("Insira o código: "))
        if N == 1:
            alcool_qtd += 1
        elif N == 2:
            diesel_qtd += 1
        elif N == 3:
            gasolina_qtd += 1
        elif N == 4:
            break
        else:
            print("Insira um número válido")
    except ValueError:
        print("Insira um número válido")

print("MUITO OBRIGADO")
print(f"Alcool: {alcool_qtd}")
print(f"Diesel: {diesel_qtd}")
print(f"Gasolina: {gasolina_qtd}")