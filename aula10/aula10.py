# Abrir arquivo
#open("nota.txt","w") 

# Abrir um arquivo e digitar informação
with open("aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Senado barra resolução que busca limitar ação dos EUA no Irã.")

# Lendo arquivo usando python
with open("aula10/nota.txt", "r") as leitura_arquivo:
    conteudo = leitura_arquivo.read()
print(conteudo)

# Escrevendo informação no final do arquivo
with open("aula10/nota.txt","a") as add_text:
    add_text.write("\nNova linha de texto.")
