from enum import Enum
class Ativo:
    def __init__(self,id, estado ):
        self.id = id 
        self.estado = estado

class EstadoAtivo(Enum):
    FALHAS_CRITICAS = "falhas criticas"
    EM_MANUTENCAO = "em manutenção"
    EM_OPERACAO = "em operação"