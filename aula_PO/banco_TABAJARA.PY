from Cliente import Cliente
# arquivo.py o nome da nossa classe
import pandas as pd

caminho_excel = "cliente_banco_Tabajara.xlsx"

print((f"\nMenu de opções:\n\n1 - Criar conta\n2 - Acessar conta\n\nOpcao digitada: \n"))

opcao = int(input("R: "))

if opcao == 1:
    print("Opcao 1 Selecionada.\n")
    nome_cliente = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ")
    tipo_conta = input("Digite seu tipo de conta, Corrente, Poupança ou Salario: ")
    numero_conta = 0
    numero_agencia = 400
    extrato_bancario = 0

    # Instancio o cliente
    cliente = Cliente(nome_cliente, cpf, tipo_conta, numero_conta, numero_agencia, extrato_bancario)

    excel = pd.DataFrame(cliente)
    excel.to_excel(caminho_excel, index=False)

elif opcao == 2:
    print("Opcao 2 Selecionada.")
