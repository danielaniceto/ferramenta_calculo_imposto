import pymysql.cursors

class ConexaoBD():
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            port=3306,
            database="aliquotassimplesnacional",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

        def get_connection(self):
            return self.connection

class ConsultaAliquotas():
    def __init__(self, conexao):
        self.connection = conexao

    def consulta_aliquota_simples_nacional_anexo01(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM aliquotas WHERE anexo_name = 'anexo01';")
                aliquotas = cursor.fetchall()
                return(aliquotas)
        except Exception as error:
            return(f"Não conseguimos consultar a aliquota no banco de dados, tente novamente {error}")
        finally:
            self.connection.close()