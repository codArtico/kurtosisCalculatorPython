from simulatedData import gerar_dados_vendas, gerar_dados_clima, gerar_dados_financas
from graphics import analisar_e_plotar

if __name__ == "__main__":
    dados_vendas = gerar_dados_vendas()
    dados_clima = gerar_dados_clima()
    dados_financas = gerar_dados_financas()

    analisar_e_plotar(dados_vendas, "A. Vendas e Negócios")
    analisar_e_plotar(dados_clima, "B. Clima (Temperaturas)")
    analisar_e_plotar(dados_financas, "C. Finanças (Retornos Diários)")
