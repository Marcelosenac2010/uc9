print("NOTAS DE 0 A 100")
Nota1 = float(input("Qual foi sua nota no primeiro trimestre \n"))
Nota2 = float(input("Qual foi sua nota no segundo trimestre \n"))
Media = (Nota1 + Nota2) / 2

if Media >= 60:
    print ("APROVADO")
else:
    print("REPROVADO")

