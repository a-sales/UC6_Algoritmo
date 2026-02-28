"""
Crie uma lista para digitar 3 itens
Adicione cada item na lista
mostre todos os itens da lista ao final
"""
# Laço de repetição
# Metodo para maniputar lista
# Lista

lista_compra = []

for i in range(3):
    item = input("Digite um item: ")
    lista_compra.append(item)

for i in lista_compra:
    print(" - ", i)



