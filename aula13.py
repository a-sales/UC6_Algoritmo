import pymysql
import pymysql.cursors

conexao = pymysql.connect(
    host="localhost", #endereço do servidor local
    user="root", #usuario do mysql
    password="",# senha do mysql
    database= "bd_livrariaonline", #nome do banco ja criado
    port=3306 #porta padrão do mysql(opcional)
)

cursor = conexao.cursor(pymysql.cursors.DictCursor)

cursor.execute("select * from clientes")
dados_cli = cursor.fetchall()

for clientes in dados_cli:
    print(clientes["nome"], clientes["data_cadastro"])