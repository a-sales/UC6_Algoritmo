# Adenilson

"""
Crie um algoritmo que leia dois números inteiros e 
verifique qual é maior e qual é o menor e imprima o 
resultado no terminal.

Exemplo: se numero1 = 4 for maior que  numero2 = 2 
então imprima no terminal a mensagem “numero1 é 
maior que número2” se for menor imprima que a 
numero1 é menor.

Faça o uso de variaveis e input
"""
"""
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))

if n1 > n2:
    print(f"O numero {n1} é maior que {n2}.")
elif n1 == n2:
    print(f"Os numero são iguais!")
else:
    print(f"O numero {n2} é maior que {n1}.")
"""
"""
Estações do ano
Crie um algoritmo onde o usuário digita um número de 
1 até 12 e retorne em tela qual é o mês correspondente 
a ele:
Exemplo de entrada: 4
Exemplo de saída: Abril
"""
"""
mes = int(input("Digite um número equivalente a Mês do Ano: "))

if mes == 12:
    print("Dezembro")
elif mes == 11:
    print("Novembro")
elif mes == 10:
    print("Outubro")
elif mes == 9:
    print("Setembro")
elif mes == 8:
    print("Agosto")
elif mes == 7:
    print("Julho")
elif mes == 6:
    print("Junho")
elif mes == 5:
    print("Maio")
elif mes == 4:
    print("Abril")
elif mes == 3:
    print("Março")
elif mes == 2:
    print("Fevereiro")
elif mes == 1:
    print("Janeiro")
else:
    print("O mês digitado é invalido")
"""

"""
Crie um programa em Python que receba um número 
inteiro do usuário e determine: “É par ou é ímpar?”
O programa deve exibir na tela se o número informado 
é par ou ímpar.
num1 % 2 = 0 (par)
"""

n = int(input("Digite um número: "))
r = n % 2
mensagem = "O número é impar" if n else "O número digitado é par!"
print(mensagem)
# if n:
#     print("O número é impar")
# else:
#     print("O número digitado é par!")
