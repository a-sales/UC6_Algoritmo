# Atividade 1 — Salvar Cadastro
# Crie um programa que:
# Peça nome e idade
# Salve no arquivo cadastros.txt
# Cada cadastro deve ficar em uma linha
# Dica de código

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    opcao = input("Deseja sair, digite SAIR para Sim: ")
    with open("aula10/cadastros.txt", "a") as cadastro:
        cadastro.write(f"nome: {nome}, idade: {idade}\n")
    if opcao == "SAIR":
        with open("aula10/cadastros.txt", "r") as leitura:
            print(leitura.read())
        break
