import sqlite3

# cria/conecta ao arquivo banco.db
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# cria uma tabela
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Islan", 18))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("João", 20))

conn.commit()
conn.close()
