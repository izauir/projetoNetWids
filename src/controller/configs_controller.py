from src.connection import Connection
from flask import Blueprint, request, jsonify


class ConfigController:
    configs = Blueprint('configs', __name__)

    def __init__(self):
        self.cursor = Connection.connectar

    @configs.route('/configs', methods=['GET'])
    def list(self):
        try:
            self.cursor.execute("SELECT * FROM configs")

            resultados = self.cursor.fetchall()

            for linha in resultados:
                print(linha)

            self.cursor.close()
            # conexao.close()

            return resultados
        except:
            print("Erro ao listar dados!")

    @configs.route('/configs', methods=['POST'])
    def insert(self):
        try:

            sql = "INSERT INTO configs (coluna1, coluna2) VALUES (%s, %s)"
            valores = ("valor1", "valor2")

            self.cursor.execute(sql, valores)

            # conexao.commit()

            print("Dados inseridos com sucesso!")

            self.cursor.close()
            # conexao.close()
        except:
            print("Erro ao inserir dados!")

    @configs.route('/configs', methods=['PUT'])
    def update(self):
        try:
            sql = "UPDATE configs SET coluna1 = %s WHERE coluna2 = %s"
            valores = ("novo_valor", "valor_antigo")

            self.cursor.execute(sql, valores)

            # conexao.commit()

            print("Dados atualizados com sucesso!")

            self.cursor.close()
            conexao.close()
        except:
            print("Erro ao atualizar dados!")

    @configs.route('/configs', methods=['DELETE'])
    def delete(self):
        try:
            sql = "DELETE FROM nome_da_tabela WHERE coluna1 = %s"
            valores = ("valor_para_excluir",)

            self.cursor.execute(sql, valores)

            conexao.commit()

            print("Dados excluídos com sucesso!")

            self.cursor.close()
            conexao.close()
        except:
            print("Erro ao excluir dados!")
