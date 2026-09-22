import math

Base = float(input("qual a base: \n"))
Altura = float(input("qual a altura: \n"))
Area = Base * Altura
Perimetro = (Base * 2) + (Altura*2)
Diagonal = math.sqrt(Base**2 + Altura**2)

print(f"Área = {Area:.2f}")
print(f"Perimetro = {Perimetro:.2f}")
print(f"Diagonal = {Diagonal:.2f}")