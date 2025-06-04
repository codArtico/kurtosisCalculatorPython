import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import numpy as np
import psycopg2 #type: ignore
import os
from dotenv import load_dotenv
from src.simulatedData import *
from src.model.connection import *

# Carregar variáveis do arquivo .env
load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# Conexão com banco PostgreSQL (modifique seus parâmetros)
conn = conectar_db()
cur = conn.cursor()

# Cria tabelas (caso não existam)
cur.execute("""
CREATE TABLE IF NOT EXISTS tb_vendas (
    id SERIAL PRIMARY KEY,
    valor NUMERIC NOT NULL
);
CREATE TABLE IF NOT EXISTS tb_clima (
    id SERIAL PRIMARY KEY,
    temperatura FLOAT NOT NULL,
    periodo VARCHAR(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS tb_financas (
    id SERIAL PRIMARY KEY,
    retorno FLOAT NOT NULL
);
""")
conn.commit()

vendas = gerar_dados_vendas()

temperaturas = gerar_dados_clima()
periodos = ['verao']*100 + ['inverno']*100

retornos = gerar_dados_financas()

# Vendas
for valor in vendas:
    cur.execute("INSERT INTO tb_vendas (valor) VALUES (%s)", (float(valor),))

# Clima
for temp, periodo in zip(temperaturas, periodos):
    cur.execute("INSERT INTO tb_clima (temperatura, periodo) VALUES (%s, %s)", (float(temp), periodo))

# Finanças
for ret in retornos:
    cur.execute("INSERT INTO tb_financas (retorno) VALUES (%s)", (float(ret),))

conn.commit()
cur.close()
conn.close()

print("Dados inseridos com sucesso!")