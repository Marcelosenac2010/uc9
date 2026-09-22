x = int(input("Valor de X: "))
y = int(input("Valor de Y: "))

# O loop deve continuar ENQUANTO ambos forem diferentes de zero
while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("Coordenadas em Q1")
    elif x < 0 and y > 0:
        print("Coordenadas em Q2")
    elif x < 0 and y < 0:
        print("Coordenadas em Q3")
    else:
        print("Coordenadas em Q4")
    
    # Nova leitura ao FINAL do loop para a próxima repetição
    x = int(input("Valor de X: "))
    y = int(input("Valor de Y: "))