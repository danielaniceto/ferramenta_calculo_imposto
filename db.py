import pymysql.cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    port=3306,
    database="aliquotassimplesnacional",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    )

def connectionBD():
    try:
        with connection.cursor as cursor:
            cursor.execute("create table aliquotas_simples_nacional")
        return f"Tabela criada com sucesso"

    except Exception as error:
        return f"Não foi possível conectar ao banco de dados, {error}"
    
connection.close()
