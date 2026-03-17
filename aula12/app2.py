import pandas as pd

def dado():
    nome = str(input("Digite seu nome: "))
    idade = str(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    return {"nome": nome, "idade": idade, "altura": altura}

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
    r_dados = dado()

    excel = pd.DataFrame(r_dados)     # Formato Excel que o python entende.

    excel.to_excel("aula12\Alunos.xlsx", index = False)

elif opcao == "2":
    print("Opção 2 Selecionada!")
    r_dados = dado()
    leitura_excel = pd.read_excel("aula12\Alunos.xlsx")
    linha = len(leitura_excel)
    print(r_dados)
    leitura_excel.loc[linha, "nome"] = r_dados["nome"]
    leitura_excel.loc[linha, "idade"] = r_dados["idade"]
    leitura_excel.loc[linha, "altura"] = r_dados["altura"]
    leitura_excel.to_excel("aula12\Alunos.xlsx", index = False)

    print(leitura_excel["nome"])

elif opcao == "3":
    print("Opção 3 Selecionada!")
elif opcao == "4":
    print("Opção 4 Selecionada!")
else:
    print("Opção invalida!")