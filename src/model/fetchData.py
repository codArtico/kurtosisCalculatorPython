import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.model.connection import conectar_db

def buscar_dados_vendas():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT valor FROM tb_vendas")
    dados = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return dados

def buscar_dados_clima():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT temperatura FROM tb_clima")
    dados = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return dados

def buscar_dados_financas():
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT retorno FROM tb_financas")
    dados = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return dados
