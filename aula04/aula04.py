
"""
nome = input("Digite seu nome: ")
print("Seu nome é: ", nome)

n = int(input("Digite um numero de 1 até 10: "))
r = n + 10
print(r)

calculo_salario = float(input("Digite o seu salario: "))
soma_salario = calculo_salario * 3.5
print(soma_salario)


idade = 16
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade"!)


# IF - ELIF - ELSE
nota = int(input("Digite a nota do aluno: "))
nome_aluno = input("Digite o nome do aluno: ")

if nota >= 9:
    print(f"O aluno {nome_aluno} está Aprovado com a nota {nota}, Excelente!")
elif nota >= 7:
    print(f"O aluno {nome_aluno} está Aprovado com a nota {nota}, Bom!")
elif nota >= 5:
    print(f"O aluno {nome_aluno} está Aprovado com a nota {nota}!, Regular")
else:
    print(f"O aluno {nome_aluno} está Reprovado com a nota {nota},!")


# Se o usuário for menor de idade então ele precisa ter autorização.
# Se o usuário for maior de idade então ele precisa ter a altura minima.

idade_cliente = int(input("Digite a idade do cliente: "))
altura_cliente = float(input("Digite a alturado do cliente: "))

if idade_cliente < 18:
    print("O Cliente é menor de idade e não pode entrar no briquedo!")
else:
    #print("Cliente maior de idade pode subir no briquedo!")
    if altura_cliente >= 1.50:
        print("Voce é maior de idade e entrar no briquedo!")
    else:
        print("Mesmo sendo maior de idade, não tem mais de 1.50 de altura!")
"""
# idade = 18
# mensagem = "Verdadeiro, Maior de idade." if idade >= 18 else "Falso, Menor de idade."
# print(mensagem)