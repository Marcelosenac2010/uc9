a = int(input("Qual o valor que você deseja descobrir a tabuada? \n"))

for i in range(1, 11):
    mult = i * a
    print(f"{i} x {a} = {mult}")