print("BEM-VINDOS AO MERCADO DO SENAC\n ")
V_unitario = float(input("Preço unitário do produto \n"))
Quantidade = float(input("Quantidade \n"))
Dinheiro = float(input("Me de o dinheiro \n"))
Total = V_unitario * Quantidade
Troco = Dinheiro - Total 
print(f"pega seu troco {Troco:.2f}")