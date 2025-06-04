# Kurtosis Calculator 📊

Este projeto é uma aplicação Python para **análise de curtose** (distribuição de dados) utilizando conjuntos simulados de vendas, clima e finanças. Ele se conecta a um banco de dados PostgreSQL, realiza análises estatísticas com `SciPy`, e exibe visualizações gráficas usando `matplotlib` e `seaborn`.

## 📁 Estrutura do Projeto

```
kurtosisCalculator/
├── src/
│   ├── graphics.py         # Função para analisar e plotar distribuições com curtose
│   ├── main.py             # Script principal
│   ├── model/
│   │   ├── connection.py   # Função de conexão ao PostgreSQL usando dotenv
│   │   ├── fetchData.py    # Busca dados do banco
│   │   └── initBD.py       # Cria tabelas e insere dados simulados
│   └── simulatedData.py    # Gera dados aleatórios para vendas, clima e finanças
├── .env                    # Variáveis de ambiente (não incluso no Git)
├── requirements.txt        # Bibliotecas necessárias
└── README.md               # Este arquivo
```

## 🚀 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/codArtico/kurtosisCalculatorPython.git
cd kurtosisCalculatorPython
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure o arquivo `.env`:**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo (substitua pelos dados do seu banco PostgreSQL):

```dotenv
DB_NAME=seubanco
DB_USER=seuusuario
DB_PASSWORD=suasenha
DB_HOST=localhost
DB_PORT=5432
```

5. **Execute o projeto:**

```bash
python src/main.py
```

O script irá:
- Inicializar o banco e popular com dados simulados;
- Realizar análises de curtose sobre os dados de vendas, clima e finanças;
- Exibir gráficos interativos com os histogramas e curvas de densidade.

## 📦 Requisitos

- Python 3.10+
- PostgreSQL
- Bibliotecas:
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `seaborn`
  - `psycopg2`
  - `python-dotenv`

## 📊 Exemplos de análise

Os gráficos exibidos mostram:
- A distribuição dos dados;
- A linha da média;
- O valor da **curtose**, que indica o grau de achatamento da curva.

## 🧠 O que é curtose?

Curtose é uma medida estatística que indica o formato da distribuição dos dados:
- Curtose > 3: distribuição com caudas pesadas (leptocúrtica);
- Curtose < 3: distribuição mais achatada (platicúrtica);
- Curtose = 3: distribuição normal (mesocúrtica).

## 👨‍💻 Autor

- [@codArtico](https://github.com/codArtico)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
