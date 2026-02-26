# Dicionarios em Python

aluno = {
    #"chave": valor
    "nome": "Pedro",
    "ano_nacimento": 1993,
    "idade": 19,
    "nota": 8,
    "curso": "TÉCNICO EM INFORMÁTICA PARA INTERNET",
    # Array
    "array": [30, True, "Texto"],
    # Dicionario dentro de outro.
    "endereco": {
        "Rua": "Rua do Senac",
        "numero": 45,
        "cidade": "São Paulo",
        "estado": "SP"
    }
}

print(aluno)                                # Exibindo todo os atributos dentro do dicionário.
print("\n",aluno["nome"])                   # Exibindo um atributo dentro do dicionário.
print(aluno["array"][1])                    # Exibindo um item dentro do array.
print("\n",aluno["endereco"]["cidade"])     # Exibindo um atributo dentro de outro dicionário.

# Alterando valor dento do dicionário
aluno["idade"] = 20
print("\n", aluno["idade"])

# Alterando dados dentro de um array
aluno["array"][1] = False
print("\n", aluno["array"][1])

# Alterando dados do diionário endereço dentro do dicionário aluno
aluno["endereco"]["cidade"] = "São Bernardo do Campo"
print("\n", aluno["endereco"]["cidade"])

# CRUD

# Adicionar um novo campo
aluno["periodo"] = "Noturno"
print("\n", aluno)

# Deletando atributo do dicionário
del aluno["idade"], aluno["endereco"]
print("\n", aluno)

# Percorrendo um dicionário
print("\n")
for chave in aluno:             # Exibindo o nome dos atributos
    print(chave)
print("\n")
for chave in aluno:
    print(aluno[chave])         # Exibindo o conteúdo dos atributos
print("\n")
for valor in aluno.values():
    print(valor)                # Exibindo o conteúdo dos atributos
print("\n")

# Percorrendo um dicionário e retornar chave e valor
for chave, valor in aluno.items():
    print(chave, " : ", valor)