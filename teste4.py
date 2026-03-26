import pandas as pd

caminho_conta   = "aula14/BANCO/Base_numero_conta.xlsx"
caminho_agencia = "aula14/BANCO/Base_numero_agencia.xlsx"

# Teste n_conta
df_conta = pd.read_excel(caminho_conta)
print("Linhas em conta:", len(df_conta))
print("Colunas em conta:", df_conta.columns.tolist())
print("Conteudo:\n", df_conta)

# Teste n_agencia
df_agencia = pd.read_excel(caminho_agencia)
print("\nLinhas em agencia:", len(df_agencia))
print("Colunas em agencia:", df_agencia.columns.tolist())
print("Conteudo:\n", df_agencia)