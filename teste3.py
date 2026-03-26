import pandas as pd
import os

caminho_banco   = "aula14/BANCO/Base_BANCO_TABAJARA.xlsx"
caminho_conta   = "aula14/BANCO/Base_numero_conta.xlsx"
caminho_agencia = "aula14/BANCO/Base_numero_agencia.xlsx"

# Teste 1 — arquivos existem?
print("Banco existe:", os.path.exists(caminho_banco))
print("Conta existe:", os.path.exists(caminho_conta))
print("Agencia existe:", os.path.exists(caminho_agencia))

# Teste 2 — consegue ler os arquivos?
df_banco   = pd.read_excel(caminho_banco)
df_conta   = pd.read_excel(caminho_conta)
df_agencia = pd.read_excel(caminho_agencia)

print("\nBanco:\n", df_banco)
print("\nConta:\n", df_conta)
print("\nAgencia:\n", df_agencia)

# Teste 3 — simula um cadastro sem input
nome_cliente     = "Teste Silva"
cpf              = "123.456.789-00"
tipo_conta       = "Corrente"
numero_conta     = 1
numero_agencia   = 1
extrato_bancario = float(0)

nova_linha = pd.DataFrame([{
    "nome_cliente":     nome_cliente,
    "tipo_conta":       tipo_conta,
    "numero_conta":     numero_conta,
    "cpf":              cpf,
    "agencia":          numero_agencia,
    "extrato_bancario": extrato_bancario
}])

df_banco = pd.concat([df_banco, nova_linha], ignore_index=True)
df_banco.to_excel(caminho_banco, index=False)
print("\nCadastro simulado com sucesso!")
print(df_banco)