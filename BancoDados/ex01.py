import sqlite3


conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()


cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS aluno(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL,
        endereco TEXT
    ) 
""")

conexao.commit()


alunos = [
    ("Marcelo", "Engenharia civil", ""),
    ("Jorge", "Geologia", "Lomba Grande"),
    ("Gabriel", "Político", "NH") ]

cursor.executemany("""
    INSERT INTO aluno (nome, curso, endereco)
    VALUES (?,?,?)
""", alunos)


print("Conexão, criação da tabela e inserção de dados realizadas com sucesso!")

cursor.execute("SELECT * FROM aluno")
resultado_db = (cursor.fetchall())
for resultados in resultado_db:
    print(f"Nome do {resultados[0]} º aluno, chamado {resultados[1]}")
conexao.commit()
conexao.close() 