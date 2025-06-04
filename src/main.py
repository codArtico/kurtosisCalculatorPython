import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model.fetchData import buscar_dados_clima, buscar_dados_financas, buscar_dados_vendas
from graphics import analisar_e_plotar
from model.initBD import initDB

if __name__ == "__main__":
    initDB()
    dados_vendas = buscar_dados_vendas()
    dados_clima = buscar_dados_clima()
    dados_financas = buscar_dados_financas()

    analisar_e_plotar(dados_vendas, "A. Vendas e Negócios")
    analisar_e_plotar(dados_clima, "B. Clima (Temperaturas)")
    analisar_e_plotar(dados_financas, "C. Finanças (Retornos Diários)")
