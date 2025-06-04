from scipy.stats import kurtosis # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np

def analisarEPlotar(dados, titulo, tipo):
    dados_np = np.array(dados, dtype=np.float64)  # converte explicitamente para float
    curt = kurtosis(dados_np)

    plt.figure(figsize=(8, 5))
    sns.histplot(dados_np, kde=True, color='skyblue', bins=30, stat='density')
    plt.axvline(np.mean(dados_np), color='red', linestyle='--', label='Média')
    plt.title(f'{titulo}\nCurtose: {curt:.2f}')
    plt.xlabel(tipo)
    plt.ylabel('Densidade')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

