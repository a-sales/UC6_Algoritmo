import random
# Exercicio
# Solicitar ao usuário um numero de 1 até 5
# Gerar um numero aleatório usando a biblioteca random
# randint
# Verificar se o usuário digitou o mesmo valor que o resultado da função randint

num_usuario = int(input("Digite um numero de 1 até 5: "))
num_aleatorio = random.randint(1,5)
if num_usuario == num_aleatorio:
    print("Parabéns, voce acertou")
    ganhou = True
else:
    print(f"Voce errou, tente novamente: {num_aleatorio}")