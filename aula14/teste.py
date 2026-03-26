import pandas as pd

nc = 1
def teste():
        #dados = {"test_id": [nc]}
        #df = pd.DataFrame(dados)
        #df.to_excel("aula14\Base_teste.xlsx", index = False)
        
        leitura_excel = pd.read_excel("aula14\Base_teste.xlsx")

        nova_linha = len(leitura_excel)   
        leitura_excel.loc[nova_linha, "test_id"] = i

        leitura_excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)

        
        print(leitura_excel)

teste()