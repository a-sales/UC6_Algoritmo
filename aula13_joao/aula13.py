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

# for clientes in dados_cli:
#     print(clientes["nome"], clientes["data_cadastro"])

# Buscar um único registro por id

# cursor.execute("SELECT nome, cidade FROM clientes WHERE id_cliente = 1")
# cliente = cursor.fetchone()
# print(cliente)

# Buscar com filtro dinâmico seguro
nome_busca = "ursula%"
#cursor.execute("SELECT * FROM clientes WHERE nome = %s", (nome_busca,))
cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", (nome_busca,))
resultado = cursor.fetchall()
print(resultado)