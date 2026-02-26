# Adenilson

# Criar um dicionário com dados digitados pelo usuário.
# Peça ao usuário:
# • nome
# • idade
# • cidade
# Guarde em um dicionário e mostre na tela.
"""
usuario = {
    "nome": " ",
    "idade": " ",
    "cidade": " "
}

for i in usuario:
    usuario[i] = input(f"Digite o {i} :")
print("\n")
for c, v in usuario.items():
    print(f"{c} : {v}")
print("\n")
"""
# Criar um dicionário com dados digitados pelo usuário.
# • nome do aluno
# • nota1
# • nota2
# • nota3
# • nota4
# • nota5
# Depois calcule e mostre a média.

aluno = {
    "nome": " ",
    "n1": " ",
    "n2": " ",
    "n3": " ",
    "n4": " ",
    "n5": " "
}
c = True
for i in aluno:
    if c:
        aluno[i] = input(f"Digite o {i}: ")
    else:
        aluno[i] = int(input(f"Digite o {i}: "))
    c = False
#print(aluno)
print("\n")
media = ( aluno["n1"] + aluno["n2"] + aluno["n3"] + aluno["n4"] + aluno["n5"] ) / 5
print(f"O resultado da média é {media}")
print("\n")