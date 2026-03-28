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

-------------------------------------------------- SEGUNDA PARTE --------------------------------------------------

Quando o usuário selecionar a opção "2 - Acessar conta" e o campo cpf e numero_conta forem encontrados na base, além de mostrar a mensagem acima, mostre um menu com as seguintes opções:

1 - Saque
2 - Deposito
3 - Saldo

Regras para cada opção
1 - Saque > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante:
- O valor solicitado para saque não pode ser maior que o valor em conta(coluna extrato_bancario), se for digitado um valor maior encerre o fluxo e mostre a mensagem "Valor maior que o disponivel em conta";
- Se o valor for menor que o disponivel em conta, realizar a subitração do valor - o valor na coluna coluna extrato_bancario, quando a operação for realizada com sucesso mostre a mensagem 
print("================================================")
print(      Saque realizado com sucesso!)
print(      Saque: (valor Solicitado)
print(      Valor em conta: (coluna extrato_bancario))
print(      Taxa para saque: (seguir regras para cada conta))
print(      Valor de desconto saque: (seguir regras para cada conta))
print("================================================\n")

OBS: Criar a logica de desconto da taxa para cada conta especifica

2 - Deposito > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante, se o valor for valido então somar com o valor já existente na coluna "extrato_bancario" e mostrar o valor final da conta bancaria(coluna extrato_bancario);
- Se o usuário digita um número negativo então encerre o fluxo e mostre a mensagem "Numero invalido, operação encerrada";


3 - Saldo > Mostre em tela o seguinte template
print("================================================")
print("   Tipo conta: (coluna tipo_conta)")
print("   Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")
"""
import pandas as pd


caminho_conta = "aula14\BANCO\Base_numero_conta.xlsx"
caminho_agencia = "aula14\BANCO\Base_numero_agencia.xlsx"
caminho_banco = "aula14\BANCO\Base_BANCO_TABAJARA.xlsx"

def n_conta():
    df = pd.read_excel(caminho_conta)

    if len(df) == 0:
        nc = 1
    else:
        nc = int(df["numero_conta"].iloc[-1]) + 1

    if nc > 100:
        print("Limite de 100 contas atingido!")
        return None

    # Sobrescreve o arquivo com apenas o último número
    pd.DataFrame([{"numero_conta": nc}]).to_excel(caminho_conta, index=False)
    return nc

def n_agencia():
    df = pd.read_excel(caminho_agencia)

    if len(df) == 0:
        na = 1
    else:
        na = int(df["numero_agencia"].iloc[-1]) + 1

    if na < 400 and na > 700:
        print("Limite de 100 agências atingido!")
        return None

    # Sobrescreve o arquivo com apenas o último número
    pd.DataFrame([{"numero_agencia": na}]).to_excel(caminho_agencia, index=False)
    return na

while True:
    opcao = input(f"\nMenu de opções:\n\n1 - Criar conta\n2 - Acessar conta\n\nOpcao digitada: ")
    if opcao == "1":
        print("\n1 - Criar conta\n")
        nome_cliente = input("Digite seu nome completo: ")
        cpf = input("Digite seu CPF: ")
        tipo_conta = input("Digite seu tipo de conta, Corrente, Poupança ou Salario: ")

        numero_conta = n_conta()
        numero_agencia = n_agencia()
        extrato_bancario = float(0)
        deposito = float(0)
        saque = float(0)

        if None in [nome_cliente, cpf, tipo_conta, numero_conta, numero_agencia, deposito, saque]:
            print("Erro: algum dado está vazio, cadastro cancelado!")
            continue

        leitura_excel = pd.read_excel(caminho_banco)
        nova_linha = pd.DataFrame([{
            "nome_cliente":     nome_cliente,
            "tipo_conta":       tipo_conta,       # ← seguindo a ordem do Excel
            "numero_conta":     numero_conta,
            "cpf":              cpf,
            "agencia":          numero_agencia,
            "extrato_bancario": extrato_bancario,
            "deposito":         deposito,
            "saque":            saque
        }])

        leitura_excel = pd.concat([leitura_excel, nova_linha], ignore_index=True)
        leitura_excel.to_excel(caminho_banco, index=False)
        print("\nCadastro realizado com sucesso!")
        #print(leitura_excel)
        
        print(f"\nDados: {nome_cliente} | {cpf} | {tipo_conta} | {numero_conta} | {numero_agencia} | {extrato_bancario}")

    elif opcao == "2":
        print("\n2 - Acessar conta\n")
        cpf          = input("Digite seu CPF: ")
        numero_conta = int(input("Digite o numero da sua conta: "))

        leitura_excel = pd.read_excel(caminho_banco, dtype={"cpf": str})  # ← força CPF como string

        resultado = leitura_excel[
            (leitura_excel["cpf"] == cpf) & 
            (leitura_excel["numero_conta"] == numero_conta)
        ]

        if len(resultado) > 0:
            print("\nBem-vindo", resultado["nome_cliente"].values[0])
            # print("Usuário encontrado!")
            # print("Nome:", resultado["nome_cliente"].values[0])
            # print("CPF:", resultado["cpf"].values[0])
            # print("Conta:", resultado["numero_conta"].values[0])
            # print("Agência:", resultado["agencia"].values[0])
            # print("Tipo:", resultado["tipo_conta"].values[0])
            # print("Saldo:", resultado["extrato_bancario"].values[0])
            # print("Deposito:", resultado["deposito"].values[0])
            # print("Saque:", resultado["saque"].values[0])
            numero_conta = resultado["numero_conta"].values[0]
            extrato_bancario = resultado["extrato_bancario"].values[0]

##################### Segunda Parte Inicio #####################

            oc = input("\nEscolha uma operação\n\n\t1 - Saque\n\t2 - Deposito\n\t3 - Saldo\n\nopção: ")
            if oc == "1":
                print("\nOpção selecionada: 1 - Saque\n")
                while True:
                    valor_saque_tmp = input("\nDigite um valor para realizar o saque: ")
                    if valor_saque_tmp.isnumeric():
                        valor_saque = float(valor_saque_tmp)
                        test_saque = extrato_bancario - (valor_saque * 1.05)
                        taxa_saque = valor_saque * 1.05
                        if test_saque >= 0:
                            print("\nSaque ", valor_saque , "Com taxa: ", taxa_saque ," Saldo: ", test_saque)
                            mascara = leitura_excel["numero_conta"] == numero_conta
                            if mascara.any():
                                leitura_excel.loc[mascara, "extrato_bancario"] = test_saque
                                leitura_excel.to_excel(caminho_banco, index=False)
                            else:
                                print(f"Conta {numero_conta} não encontrada no arquivo.")

                            break
                        else:
                            print("\nValor maior que o disponivel em conta")
                        #     break
                        # break
                    else:
                        print("\nValor invalido!\n")

            elif oc == "2":
                print("\nOpção selecionada: 2 - Deposito\n")
                while True:
                    valor_deposito_tmp = input("\nDigite um valor para realizar o deposito: ")
                    if valor_deposito_tmp.isnumeric():
                        valor_deposit = float(valor_deposito_tmp)
                        test_deposit = extrato_bancario + valor_deposit
                        if test_deposit != 0:
                            print("\nDeposito ", valor_deposit , " Anterior saldo: ", extrato_bancario  ," Saldo: ", test_deposit)
                            mascara = leitura_excel["numero_conta"] == numero_conta
                            if mascara.any():
                                leitura_excel.loc[mascara, "extrato_bancario"] = test_deposit
                                leitura_excel.to_excel(caminho_banco, index=False)
                            else:
                                print(f"Conta {numero_conta} não encontrada no arquivo.")

                            break
                        else:
                            print("\nValor maior que o disponivel em conta")
                        #     break
                        # break
                    else:
                        print("\nValor invalido!\n")

            elif oc == "3":
                print("\nOpção selecionada: 3 - Saldo\n")
                while True:
                    saida_extrato = float(extrato_bancario)
                    print("O Saldo em conta é: ", saida_extrato )
                    break

            else:
                print("Operação invalida!")

##################### Segunda Parte Fim #####################
        else:
            print("\nCPF ou número de conta inválido!")

    else:
        print("\nOpcao invalida, escolha uma opcao valida!\n")
