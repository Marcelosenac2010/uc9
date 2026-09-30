import sqlite3
from abc import ABC, abstractmethod
from enum import Enum

# 1. Enum com os 3 estados
class EstadoAtivo(Enum):
    FALHAS_CRITICAS = "falhas criticas"
    EM_MANUTENCAO = "em manutenção"
    EM_OPERACAO = "em operação"

# 2. Classe Base DAO
class BaseDAO(ABC):
    def __init__(self, dbconfig=None):
        self.dbconfig = dbconfig

    def get_connect(self):
        try:
            return sqlite3.connect("eam_mvc_ativos.db")
        except sqlite3.Error as err:
            raise ConnectionAbortedError(f"Problemas ao conectar: {err}")

    def criar_tabela(self):
        try:
            conexao = self.get_connect()
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Ativo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    estado TEXT NOT NULL CHECK(estado IN ('falhas criticas', 'em manutenção', 'em operação'))
                )
            """)
            conexao.commit()
            conexao.close()
        except sqlite3.Error as err:
            raise Exception(f"Erro ao criar tabela: {err}")

    @abstractmethod
    def save(self, objeto):
        pass