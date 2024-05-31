import pymysql.cursors
import mysql.connector

connection = pymysql.connect(
                             
    host="localhost",
    user="root",
    password="1234",
    port=3306,
    database="aliquotassimplesnacional",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    )

class ConexaoBD():
    def connectionBD():
        cursor = connection.cursor
        cursor.execute(connection)

    def consulta_aliquota_simples_nacional():
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM aliquotasimplesnacional WHERE AliquotaAnexo01")
                aliquotas = cursor.fetchall()
                for aliquota in aliquotas:
                    return(aliquota)
        except Exception as error:
            return(f"Não conseguimos consultar a aliquota no banco de dados, tente novamente {error}")