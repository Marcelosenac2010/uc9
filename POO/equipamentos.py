class Equipamento:
    def __init__(self, patrimonio, fabricante, ano_aquisicao):
        self.patrimonio = patrimonio
        self.fabricante = fabricante
        self.ano_aquisicao = ano_aquisicao

    def detalhes(self):
        return f"Patrimônio: {self.patrimonio}\n" \
               f"Fabricante: {self.fabricante}\n" \
               f"Ano de aquisição: {self.ano_aquisicao}"


class Notebook(Equipamento):
    def __init__(self, patrimonio, fabricante, ano_aquisicao, memoria_ram):
        super().__init__(patrimonio, fabricante, ano_aquisicao)
        self.memoria_ram = memoria_ram

    def detalhes(self):
        return f"Patrimônio: {self.patrimonio}\n" \
               f"Fabricante: {self.fabricante}\n" \
               f"Ano de aquisição: {self.ano_aquisicao}\n" \
               f"Memória RAM: {self.memoria_ram} GB"


notebook = Notebook("TI-1025", "Dell", 2025, 16)

print(notebook.detalhes())