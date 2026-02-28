"""
Dicionario {} -> Para acessar os dados usamos o nome da chave
Lista [] -> Para acessar os dados usamos a posição da lista
"""

notas = [ 10, 8, True, "Adenilson", 10 ]
#          0  1   2         3

notas.append("Sales")       # Inserindo informação no final do array
print(notas[4])

notas.insert(0, False)      # Inserindo informação em uma posição que desejar
print(notas)
"""
nova_lista = [ "Óla", 1993, 24.50 ]
nova_lista.extend(notas)            # Juntando dois arrays
tudo_junto = notas + nova_lista     # Outra forma de fazer o mesmo
print(tudo_junto[0])
#print(nova_lista)


notas.remove("Sales")               # Removendo a primeira do ocorrencia de um valor, case sensitive
print(notas)
"""
nome_numeros = [ 390, "Adenilson", 19, "Ana,", 45, "Iara", 390 ]
nome_numeros.pop(2)                 # Remoto o ultimo valor se estiver vazio ou o indice indicado
print(nome_numeros)

#print(nome_numeros.clear())         # Limpa todos os valores do array

print(nome_numeros.index(390))      # Retorna o indice onde o primeiro valor foi encontrado

print(nome_numeros.count(390))      # Buscar quantas vezes o valor foi encontrado dentro do array

nums = [ 5, 9, 2, 3 ]
nums.sort()                         # Ordenando numeros dentro do array
print(nums)

nomes = [ "c", "a", "e", "b" ]
nomes.sort()                         # Ordenando nomes dentro do array
print(nomes)


nums.reverse()                      # Inverte a ordem do array do final para o começo
print(nums)

nomes.reverse()
print(nomes)

