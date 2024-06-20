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

    def close_connection(self):
        self.connection.close()

class ConsultaAliquotas:
    def __init__(self):
        conn = ConexaoBD
        self.connection:pymysql.connect = conn.get_connection

    def consulta_aliquota_simples_nacional(self, anexo):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM aliquotas WHERE anexo_name = '{anexo}';")
                print(F"EU SOU O ANEXO DENTRO DA FUNCAO CONSULTA SIMPLES NACIONAL NO DB.PY {anexo}")
                aliquotas = cursor.fetchall()
                if not bool(aliquotas):
                    return []
                self.connection.commit()
                print(f"EU SOU A ALIQUOTA NO BD.PY{aliquotas}")
                return aliquotas

        except Exception as error:
            return(f"Não conseguimos consultar a aliquota no banco de dados, tente novamente {str(error)}")

    ConexaoBD.close_connection
