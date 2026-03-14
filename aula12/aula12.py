import pandas as pd

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# Criação de um dicionário para receber os dados digitados pelo usuário
dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}

#excel = pd.DataFrame(dados)

# to_excel() serve criar uma nova planilha, pegar os dados digitados pelo usuário em formato DataFrame e gravar na planilha criada.

# excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)

# Ler os dados

leitura_excel = pd.read_excel("aula12\cadastro_alunos.xlsx")

# Conta a quantas linha existem no excel e cria uma nova linha para receber a nova informação digitada pelo usuário

nova_linha = len(leitura_excel)         

leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

leitura_excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)
