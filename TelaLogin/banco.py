import mysql.connector
from mysql.connector import Error

def Conectar(self):
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sistema_db'
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def cadastrar (nome, senha):
    conexao = Conectar(None)
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = "INSERT INTO USUARIO (nome, senha) VALUES (%s, %s)"
        cursor.execute(query, (nome, senha))
        conexao.commit()
        return True
    except Error as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

def validar_login(nome, senha):
    conexao = Conectar(None)
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM USUARIO WHERE nome = %s AND senha = %s"
        cursor.execute(query, (nome, senha))
        resultado = cursor.fetchone()
        return resultado is not None
    except Error as e:
        print(f"Erro ao executar a consulta: {e}")
        return False
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()