import requests

# Data da entrega: 15/03/2025

# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""

# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])



# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":
]
"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""
n=0
dig = "a"
while True:
    print("\nMenu de opções:\n\n1 - Consultar por ID.\n2 - Consultar por nome.\n3 - Lista de personagens.\n")
    if dig.isnumeric():
        opcao = int(dig)
        print(opcao)
        if opcao == 1:
            id = int(input("Digite o ID do personagem: "))
            url_api = f"https://rickandmortyapi.com/api/character/{id}"
            resultado = requests.get(url_api)
            json = resultado.json()

            for i in json:
                print(f"{i} : {json[i]}")

        elif opcao == 2:
            name = input("Digite o nome do personagem: ")
            url_api = f"https://rickandmortyapi.com/api/character/"
            resultado = requests.get(url_api)
            json = resultado.json()

            for i in json["results"]:
                id_tmp = i["id"]
                if i["name"] == name:
                    id = id_tmp
            
            url_api = f"https://rickandmortyapi.com/api/character/{id}"
            resultado = requests.get(url_api)
            json = resultado.json()

            for i in json:
                print(f"{i} : {json[i]}")

        elif opcao == 3:
            url_api = f"https://rickandmortyapi.com/api/character/"
            resultado = requests.get(url_api)
            json = resultado.json()
            print(json["results"])

            for i in json["results"]:
                for r in i:
                    print(f"{r} - {i[r]}")
                print("\n")
            break

        else:
            print("\nNenhuma opção selecionada.\n")
            dig = "a"

    else:
        dig = input("Escolha uma numero: ")
        