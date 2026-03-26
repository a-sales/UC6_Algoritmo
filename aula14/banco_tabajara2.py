#  Banco Tabajara
# Nome pasta: BANCO
# Nome do arquivo: banco_tabajara.py
# Nome do excel: base_BANCO_TABAJARA

# Vamos criar um sistema bancário chamado banco tabajara, nosso banco terá as seguintes caracteristicas:

"""
Contas:
- Corrente
- Poupança
- Salario

Dados do cliente que vamos guardar em um excel:
- nome_cliente
- tipo_conta
- numero_conta
- cpf
- agencia
- extrato_bancario
- deposito
- saque

Obs: Esse serão os nomes das colunas no nosso excel

Seguintes regras de saque para cada conta:
Saques na conta Corrente: 5% de taxa
Saques na conta Corrente: Poupança 0% de taxa
Saques na conta Corrente: Salario 2% de taxa

Crie um menu com as seguintes opções:
1 - Criar conta
2 - Acessar conta

######### Desenvolvimento #########

Regras para cada opção no menu
1 - Criar conta > Solicitar ao usuario digitar as seguintes informações:
- nome_cliente
- cpf
- tipo_conta

O outros campos serão gerados de forma automatica
- numero_conta = Será gerada de forma sequencial começando do 0 até 100
- agencia = será gerado de forma sequencial começando do 400 até 700
- extrato_bancario = valor inicial terá que começar em 0

Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario

2 - Acessar conta > É necessário que o usuário passe os seguites dados:
- cpf
- numero_conta
> Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara" SENAO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
"""
import pandas as pd


caminho_conta = "aula14\BANCO\Base_numero_conta.xlsx"  # um único caminho

def n_conta():
    leitura_excel = pd.read_excel(caminho_conta)
    
    if len(leitura_excel) == 0:
        print("Arquivo vazio!")
        return None
    
    # Pega o último número e incrementa
    nc = leitura_excel["numero_conta"].iloc[-1]
    nc += 1
    
    if nc <= 100:
        linha = len(leitura_excel)
        leitura_excel.loc[linha, "numero_conta"] = nc
        leitura_excel.to_excel(caminho_conta, index=False)  # ← salva no mesmo arquivo
        return nc
    else:
        print("Limite de 100 contas atingido!")
        return None
    
#test = n_conta()
#print(test)

caminho_agencia = "aula14\BANCO\Base_numero_agencia.xlsx"

def n_agencia():
    leitura_excel = pd.read_excel(caminho_agencia)
    
    if len(leitura_excel) == 0:
        print("Arquivo vazio!")
        return None
    
    # Pega o último número e incrementa
    na = leitura_excel["numero_agencia"].iloc[-1]
    na += 1
    
    if na <= 100:
        linha = len(leitura_excel)
        leitura_excel.loc[linha, "numero_agencia"] = na
        leitura_excel.to_excel(caminho_agencia, index=False)  # ← salva no mesmo arquivo
        return na
    else:
        print("Limite de 100 contas atingido!")
        return None
    
#test = n_agencia()
#print(test)

caminho_banco = "aula14\BANCO\Base_BANCO_TABAJARA.xlsx"

while True:
    opcao = input(f"\nCrie um menu com as seguintes opções:\n\n1 - Criar conta\n2 - Acessar conta\n\nOpcao digitada: ")
    if opcao == "1":
        print("\n1 - Criar conta\n")
        nome_cliente = input("Digite seu nome completo: ")
        cpf = input("Digite seu CPF: ")
        tipo_conta = input("Digite seu tipo de conta, Corrente, Poupança ou Salario: ")

        numero_conta = n_conta()
        numero_agencia = n_agencia()
        extrato_bancario = float(0)
    
        print(f"\nDados: {nome_cliente} | {cpf} | {tipo_conta} | {numero_conta} | {numero_agencia} | {extrato_bancario}")

        if None in [nome_cliente, cpf, tipo_conta, numero_conta, numero_agencia]:
            print("Erro: algum dado está vazio, cadastro cancelado!")
            continue

        leitura_excel = pd.read_excel(caminho_banco)
        nova_linha = pd.DataFrame([{
            "nome_cliente":     nome_cliente,
            "tipo_conta":       tipo_conta,       # ← seguindo a ordem do Excel
            "numero_conta":     numero_conta,
            "cpf":              cpf,
            "agencia":          numero_agencia,
            "extrato_bancario": extrato_bancario
        }])

        leitura_excel = pd.concat([leitura_excel, nova_linha], ignore_index=True)
        leitura_excel.to_excel(caminho_banco, index=False)
        print("Cadastro realizado com sucesso!")
        print(leitura_excel)

    elif opcao == "2":
        print("\n2 - Acessar conta\n")
    else:
        print("\nOpcao invalida, escolha uma opcao valida!\n")
