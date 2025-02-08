import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS dados (coluna1 TEXT, coluna2 INTEGER)''')

# Inserir dados
data.to_sql('dados', conn, if_exists='replace', index=False)

# Fechar conexão
conn.close()