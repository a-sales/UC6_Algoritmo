"""
 S  e  n  a  c  ,  .  /  ?
 0  1  2  3  4  5  6  7  8
-9 -8 -7 -6 -5 -4 -3 -2 -1 
"""

text1 = "SENAC"
print("Caracter numero um:\t\t", text1[0])
print("Caracter numero três:\t\t", text1[3])
print("Ultimo caracter do texto:\t", text1[-1])
print("Tamanho do texto escrito:\t", len(text1)) # Função Len

text2 = "هناك حقيقة مثبتة منذ زمن طويل وهي أن المحتوى المقروء لصفحة ما سيلهي القارئ عن التركيز على الشكل الخارجي للنص أو شكل توضع الفقرات في الصفحة التي يقرأها"

print("\nTexto arabe:\t", len(text2))

text3 = "Python é incrível"
print(text3.upper())        # Todo texto em maiuscula
print(text3.lower())        # Todo texto em minuscula
print(text3.capitalize())   # Primeira letra do texto em maiscula
print(text3.title())        # Todas as primeiras letras em maiscula

text4 = "Python"
print(text4[0:2])           # Py
print(text4[2:])            # thon
print(text4[:3])            # Pyt

text5 = "\nPython é incrível.\n"
novo_text5 = text5.replace("incrível", "uma cobra")     # Substituindo palavras
print(novo_text5)

text6 = "   Python   "
print(text6.strip())    # Remove espaço em branco do lado esquerda e direira.
print(text6.lstrip())   # Remove espaço em branco do lado esquerdo
print(text6.rstrip())   # Remove espaço em branco do lado direita

text7 = "Pulei carnaval, mas hoje estou estudando."
print("carnaval" in text7)      # Retorna verdadeiro ou falso se encontra o texto
print(text7.find("hoje"))       # Encontra em qual posíção começa a palavra

print(text7.count("a"))         # Conta quantas vezes o padrão se repete no texto

text8 = "Eu amo Java."
print(text8.startswith("Eu"))   # Retorna verdadeiro ou falso se o texto começa com o padrão
print(text8.endswith("."))      # Retorna verdadeiro ou falso se o texto termina com o padrão