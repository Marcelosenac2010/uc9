x = int(input(" Primeiro valor \n "))
y = int(input(" Segundo valor \n"))

while x != y:
    if x < y:
        print("crescente")
    else:
        print("decrescente")
    print (" digite mais dois valores")
    x = input("")
    y = input("")
print("\n Processo encerrado")