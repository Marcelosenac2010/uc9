class ProcessadorLotes:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        # Reinicia o contador e retorna o próprio iterador
        self.atual = 0
        return self

    def __next__(self):
        self .atual += 1
        if self.atual <= self.limite:
            return f"Lote {self.atual}"
        else:
            # Sinaliza o fim da iteração
            raise StopIteration

# --- Testando a implementação ---
if __name__ == "__main__":
    processador = ProcessadorLotes(5)
    
    # Iterando sobre o objeto com um loop for
    for lote in processador:
        print(lote)