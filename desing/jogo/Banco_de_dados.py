import sqlite3
import os

endereço = os.path.dirname(os.path.abspath(__file__))

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"



def inicializar_banco():
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,         
        altura INTEGER,
        peso INTEGER,
        classe TEXT
        
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS status (
        usuario_id INTEGER PRIMARY KEY,
        nivel INTEGER,
        dano INTEGER,
        velocidade INTEGER,
        defesa INTEGER,
        vida integer,
        arma INTEGER,
        experiencia INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progresso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        capitulo INTEGER,
        missao INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        item TEXT,
        quantidade INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        rosto INTEGER,
        camisa INTEGER,
        mao INTEGER,
        braço INTEGER,
        calça INTEGER,
        sapatos INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    conexao.commit()
    conexao.close()