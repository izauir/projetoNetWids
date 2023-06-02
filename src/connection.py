import mysql.connector


class Connection:

    def __init__(self):
        self.connectar()

    def connectar(self):
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="netwids",
            port="3308"
        )

        cursor = conexao.cursor()

        return cursor
