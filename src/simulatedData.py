import numpy as np

def gerarDadosVendas():
    np.random.seed(0)
    vendas_normais = np.random.normal(loc=100, scale=10, size=90)
    picos_black_friday = np.random.normal(loc=500, scale=30, size=10)
    return np.concatenate((vendas_normais, picos_black_friday))

def gerarDadosClima():
    temperaturas_verao = np.random.normal(loc=35, scale=5, size=100)
    temperaturas_verao[::10] += 10
    temperaturas_inverno = np.random.normal(loc=15, scale=3, size=100)
    return np.concatenate((temperaturas_verao, temperaturas_inverno))

def gerarDadosFinancas():
    retornos_normais = np.random.normal(loc=0.001, scale=0.02, size=190)
    quedas_brutas = np.random.normal(loc=-0.2, scale=0.05, size=10)
    return np.concatenate((retornos_normais, quedas_brutas))
