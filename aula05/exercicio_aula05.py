# Adenilson

# Em um arquivo exercicio_aula05.py  você terá que criar um 
# algoritmo utilizando laço de repetição e estrutura condicional para 
# criar uma tabuada, seguindo as seguintes regras:

# Seu programa precisa receber um número digitado pelo usuário, 
# verifique se esse número é válido, se o número for válido então use 
# o laço de repetição para mostrar a tabuada utilizando o número 
# que o usuário digitou se o número for inválido então mostrar a 
# mensagem “Número invalido, tente novamente”.



var = input("\nDigite um numero: ")
n = int(var) if var.isdigit() else False

if n:
    print("\n")
    for i in range(1, 11):
        r = i * n
        print(f"{n} * {i} = {r}")
    print("\n")
else:
    print("\nNumero digitado invalido.\n")