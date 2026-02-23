# Adenilson

# Contando de 1 até 10 (marcando os pares)

# Faça um programa que:
# Mostre um menu:
# 1 - Par ou Ímpar
# 2 - Tabuada
# 3 - Sair
# Continue rodando até o usuário escolher sair
"""
for i in range(1, 11):
    n = i % 2
    if n == 0:
        print(f"{i}")
"""
while True:
    print("\n1 - Par ou Ímpar\n2 - Tabuada\n3 - Sair\n")
    var = str(input("Digite um dos valores acima: "))
    if var == "1":
        n = int(input("Digite um número: "))
        r = n % 2
        if r == 0:
            print("O número digitado é par!")
        else:
            print("O número é impar!")

    if var == "2":
        var = input("\nDigite um numero: ")
        n = int(var) if var.isdigit() else False

        if n:
            print("\n")
            for i in range(1, 11):
                r = i * n
                print(f"{n} * {i} = {r}")
            print("\n")
        else:
            print("\nNumero digitado invalido.\n")

    if var == "3":
        break
