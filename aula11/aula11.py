import random
import math
import datetime

num_aleatorio = random.randint(1000,2000)
print(num_aleatorio)

# Sorteio de nomes
alunos = ["Israel", "Adenilson", "Anna", "Wellington", "Jonathan", "Isabelly", "João Pedro", "Luis Felipe", "Iara", "Vanessa", "Daniel", "João Paulo", "Lucas", "Bernardo", "Camila", "Stefany", "Guilherme", "Micael", "Kauan"]

sorteado1 = random.choice(alunos)
sorteado2 = random.choice(alunos)

# Choice escolher de forma aleatoria

print("Dupla: ", sorteado1, " - ", sorteado2)

# Usando a biblioteca Math para calculo de raiz,

numero = 144
raiz = math.sqrt(numero)
print(raiz)

# Elevando um numero

print(math.pow(4,2))

# Trabalhando com datas

agora = datetime.datetime.now()
print(agora.microsecond)