import pandas as pd

caminho_banco = "aula14/BANCO/Base_BANCO_TABAJARA.xlsx"

leitura_excel = pd.read_excel(caminho_banco)
print("Colunas do Excel:", leitura_excel.columns.tolist())  # ← mostra os nomes exatos