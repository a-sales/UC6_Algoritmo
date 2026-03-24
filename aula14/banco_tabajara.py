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


#nc = 0; na = 400
def n_conta():
    try:
        leitura_excel = pd.read_excel("aula14\BANCO\Base_numero_conta.xlsx")
        linha = len(leitura_excel)
        #nc = linha
        #nc = leitura_excel["numero_conta"]
        
        if linha < 101:
            nc += 1
            print(nc)
            #leitura_excel.loc["numero_conta"] = nc
            #leitura_excel.to_excel("aula14\BANCO\Base_numero_conta.xlsx")
            #dados = {"numero_conta": nc}
            
            leitura_excel.loc[len(leitura_excel)] =  nc
            leitura_excel.to_excel("aula14\BANCO\Base_numero_conta.xlsx")
            return(nc)
        
    except:
        nc = 0
        dados = {"numero_conta": [nc] }
        excel = pd.DataFrame(dados)
        excel.to_excel("aula14\BANCO\Base_numero_conta.xlsx", index = False)
        #print("erro")
        return(nc)
    

test = n_conta()
print(test)
"""
def n_agencia():
    leitura_excel = pd.read_excel("aula14\BANCO\base_numero_agencia.xlsx")
    linha = len(leitura_excel)
    if linha == 0:
        na = 400
        leitura_excel.loc["numero_agencia"] = na

        return(na)
    else:
        na = leitura_excel["numero_agencia"]
    if na >= 400 or na <= 700:
        na += 1
    return(na)

while True:
    opcao = input(f"\nCrie um menu com as seguintes opções:\n\n1 - Criar conta\n2 - Acessar conta\n\nOpcao digitada: ")
    if opcao == "1":
        print("\n1 - Criar conta\n")
        nome_cliente = input("Digite seu nome completo: ")
        cpf = input("Digite seu CPF: ")
        tipo_conta = input("Digite seu tipo de conta, Corrente, Poupança ou Salario: ")

        numero_conta = n_conta()
        agencia = n_agencia()
        extrato_bancario = float(0)
        print(f"\n{nome_cliente}, {cpf} e {tipo_conta}, {numero_conta}, {agencia}, {extrato_bancario}")

        # leitura_excel_conta = pd.read_excel("aula14\BANCO\base_numero_conta.xlsx")      # Lendo o valor da conta
        # lc = len(leitura_excel_conta)


        # leitura_excel_agencia = pd.read_excel("aula14\BANCO\base_numero_agencia.xlsx")  # Lendo o valor da agencia
        # la = len(leitura_excel_agencia)


        leitura_excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)

    elif opcao == "2":
        print("\n2 - Acessar conta\n")
    else:
        print("\nOpcao invalida, escolha uma opcao valida!\n")
"""