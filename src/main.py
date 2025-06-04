import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from model.fetchData import buscarDadosClima, buscarDadosFinancas, buscarDadosVendas

from model.initBD import initDB
from utils.mainUtils import verDados, switch

if __name__ == "__main__":
    initDB()

    print("Gerando dados de vendas...\n")
    dadosVendas = buscarDadosVendas()
    nome = "vendas"
    verDados(dadosVendas, nome)

    print("Gerando dados de clima...\n")
    dadosClima = buscarDadosClima()
    nome = "clima"
    verDados(dadosClima, nome)

    print("Gerando dados de finanças...\n")
    dadosFinancas = buscarDadosFinancas()
    nome = "finanças"
    verDados(dadosFinancas, nome)

    switch(dadosVendas, dadosClima, dadosFinancas)

        



    
    
    
