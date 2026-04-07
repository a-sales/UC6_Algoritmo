# Criando uma classe
class Cliente:  # A evolução de uma dicionario é a criação de uma classe.
    def __init__(self, nome_cliente, cpf, tipo_conta, numero_conta, numero_agencia, extrato_bancario): # __init__ Construtor Cria um mode dos dados do cliente, o objetivo é conseguir transferir dados por todos os arquivos python.
        # Atributos de uma classe.
        self.nome_cliente = nome_cliente 
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.numero_agencia = numero_agencia
        self.extrato_bancario = extrato_bancario
        pass

    def __str__(self):
        return (f"Nome: {self.nome_cliente} | CPF: {self.cpf} | Tipo: {self.tipo_conta} | Conta: {self.numero_conta} |  Agencia: {self.numero_agencia} | Extrato: {self.extrato_bancario}")
        