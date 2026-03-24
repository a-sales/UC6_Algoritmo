import pandas as pd

nc = 1
def teste():
        dados = {"test_id": [nc]}
        excel = pd.DataFrame(dados)
        excel.to_excel("aula14\Base_teste.xlsx", index = False)

        leitura_excel = pd.read_excel("aula14\Base_teste.xlsx")
        print(leitura_excel)

teste()