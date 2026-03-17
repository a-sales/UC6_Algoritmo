import pandas as pd

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Alterar")
print("         4 > Apagar")
opcao = input("R: ")

if opcao == "1":
    print("Opção 1 Selecionada!")
    nome = str(input("Digite seu nome: "))
    idade = str(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }

    excel = pd.DataFrame(dados)     # Formato Excel que o python entende.

    excel.to_excel("aula12\Alunos.xlsx", index = False)

elif opcao == "2":
    print("Opção 2 Selecionada!")

elif opcao == "3":
    print("Opção 3 Selecionada!")
elif opcao == "4":
    print("Opção 4 Selecionada!")
else:
    print("Opção invalida!")