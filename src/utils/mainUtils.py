import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from graphics import analisarEPlotar

def verDados(data,nome):
    key = input(f'Deseja ver dados de {nome}? S/N: ').upper()
    if key == 'S':
        print(data)
        input("\n Digite qualquer entrada para continuar: ")
    print(" ")

def verPercentual():
    key = input(f'Deseja ver em percentual? S/N: ').upper()
    return key

def switch(dadosVendas, dadosClima, dadosFinancas):
    print('1 - Analisar e plotar dados de vendas')
    print('2 - Analisar e plotar dados de clima')
    print('3 - Analisar e plotar dados de financas')
    print(" ")

    key = int(input("Digite uma opção: "))
    

    while (key == 1 or key == 2 or key==3):
        ylabel = verPercentual()
        if key == 1:
            analisarEPlotar(dadosVendas, "Loja", "Unidades", ylabel)
        elif key == 2:
            analisarEPlotar(dadosClima, "Clima", "Temperatura °C", ylabel)
        elif key == 3:
            analisarEPlotar(dadosFinancas, "Bolsa de valores", "Retornos", ylabel)

        key = int(input("Digite uma opção: "))