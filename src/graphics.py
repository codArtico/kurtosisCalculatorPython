from scipy.stats import kurtosis # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.ticker import FuncFormatter # type: ignore
import seaborn as sns # type: ignore
import numpy as np

def analisarEPlotar(dados, titulo, tipo, y):
    dados_np = np.array(dados, dtype=np.float64)  # converte explicitamente para float
    curt = kurtosis(dados_np)

    plt.figure(figsize=(8, 5))
    
    if (y) == 'S':
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y * 100:.0f}%'))
        sns.histplot(dados_np, kde=True, color='skyblue', bins=30, stat='probability')
        plt.ylabel('Percentual de dados: %')
    else:
        sns.histplot(dados_np, kde=True, color='skyblue', bins=30, stat='density')
        plt.ylabel('Densidade')
        
    plt.axvline(np.mean(dados_np), color='red', linestyle='--', label='Média')
    plt.title(f'{titulo}\nCurtose: {curt:.2f}')
    plt.xlabel(tipo)
    
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

