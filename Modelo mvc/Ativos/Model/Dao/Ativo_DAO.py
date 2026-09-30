import sqlite3
from Base_DAO import BaseDAO
from Ativo_model import EstadoAtivo  


class AtivoDAO(BaseDAO):
    
    def save(self, ativo):
        """Salva um novo ativo no banco de dados validando o estado permitido."""
        estados_permitidos = [e.value for e in EstadoAtivo]
        
        if ativo.estado not in estados_permitidos:
            raise ValueError(f"Estado inválido! Use um dos seguintes: {estados_permitidos}")

        try:
            conexao = self.get_connect()
            cursor = conexao.cursor()
            
            cursor.execute("""
                INSERT INTO Ativo (estado) VALUES (?)
            """, (ativo.estado,))
            
            conexao.commit()
            conexao.close()
            print("Ativo salvo com sucesso!")
            
        except sqlite3.Error as err:
            raise Exception(f"Erro ao salvar o ativo: {err}")

    def contar_por_estado(self, estado):
        """Busca e retorna a quantidade exata de ativos para um determinado estado usando SELECT COUNT(*)"""
        try:
            conexao = self.get_connect()
            cursor = conexao.cursor()
            
            cursor.execute("""
                SELECT COUNT(*) FROM Ativo WHERE estado = ?
            """, (estado,))
            
            # cursor.fetchone() retorna uma tupla (ex: (5,)), pegamos o primeiro elemento [0]
            quantidade = cursor.fetchone()[0]
            
            conexao.close()
            return quantidade
            
        except sqlite3.Error as err:
            raise Exception(f"Erro ao contar ativos por estado: {err}")