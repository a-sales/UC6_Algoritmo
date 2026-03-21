import pymysql as pySQL

# Aquivo para trabalhar com banco de dados e fazer operações UPDATE, INSERT e DELETE

conexao = pySQL.connect(
    host = "localhost",               # Endereço do servidor local
    user = "root",                    # Usuario do mysql
    password = "",                    # Senha do mysql
    database = "bd_livrariaonline",   # Nome do banco ja criado
    port = 3306                       # Porta padrão do mysql(opcional)
)

cursor = conexao.cursor(pySQL.cursors.DictCursor)

try:
    # INSERT: Adicionar um novo registro.
    """
    sql_insert = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    cursor.execute(sql_insert, ("teste", "teste@email.com"))
    conexao.commit()                  # Confirma o INSERT
    print("Inserindo com sucesso! ID: ", cursor.lastrowid) # Retorna o ultimo ID

        # UPDATE: Atualizar um registro existente.
    sql_update = "UPDATE clientes SET email = %s WHERE id_cliente = %s"
    cursor.execute(sql_update, ("novo@email.com", 1))
    conexao.commit()                  # Confirma o UPDATE
    print("Linhas afetadas: ", cursor.rowcount)
"""
    # DELETE: Remove um registro.
    cursor.execute("DELETE FROM compras WHERE id_compra = %s", (5,))
    conexao.commit()                  # Confirma o DELETE
    

except Exception as erro:
    conexao.rollback()                # Desfaz tudo se algo deu errado
    print("Erro! Operação revertida: ", erro)

finally:
    cursor.close()
    conexao.close()                   # Fecha conexão com o banco de dados




