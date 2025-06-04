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

def switch(dadosVendas, dadosClima, dadosFinancas):
    print('1 - Analisar e plotar dados de vendas')
    print('2 - Analisar e plotar dados de clima')
    print('3 - Analisar e plotar dados de financas')
    print(" ")
    
    key = int(input("Digite uma opção: "))

    while (key == 1 or key == 2 or key==3):
        if key == 1:
            analisarEPlotar(dadosVendas, "Loja", "Unidades")
        elif key == 2:
            analisarEPlotar(dadosClima, "Clima", "Temperatura °C")
        elif key == 3:
            analisarEPlotar(dadosFinancas, "Bolsa de valores", "Retornos")

        key = int(input("Digite uma opção: "))