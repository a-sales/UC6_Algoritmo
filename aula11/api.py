import requests

# API

url = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url)    # Retorno status 200 Ok

json = resposta.json()          # Obtendo um JSON da API

personagem = json["results"]

# for i in personagem:
    # print(i["name"])            # Acessando um item no dicionario dentro de outro dicionario

#print(personagem)
"""
for mais_info in personagem:    # Acessando mais item dentro do dicionario
    print("Nome: ",mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especie: ", mais_info["species"])
    print("---------------------------")
"""

# Pedir ao usuário para digitar um ID e retornar da API o personagem referente a esse ID

id = int(input("Digite o ID do usuário: "))
link_API = f"https://rickandmortyapi.com/api/character/{id}"
resultado = requests.get(link_API)
novo_json = resultado.json()

print("\nNome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especie: ", novo_json["species"])
print("---------------------------\n")


