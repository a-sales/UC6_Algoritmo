"""
Crie uma lista com 4 nomes
Peça ao usuário um nome para remover
Se o nome existir, remova
Senão mostre uma mensagem dizendo que o nome não existe
Mostre a lista final
"""

nome_list = [ "Adenilson", "Daniel" , "Micael", "Bernardo" ]
pesquisa = input("Digite um nome para ser pesquisado: ")
r = False
for i in nome_list:
    if pesquisa == i:
        nome_list.remove(i)
        print("Removendo: ", i)
        r=True

if r:
    print(nome_list)
else:
    print("Não foi encontrado o nome: ", pesquisa)