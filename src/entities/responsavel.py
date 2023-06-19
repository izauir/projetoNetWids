from src.entities.crianca import Crianca
from src.entities.tarefa import Tarefa


class Responsavel:
    def __init__(self, cpf, nome, endereco, login, senha):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.login = login
        self.senha = senha

    def criar_conta_crianca(self, id, nome, idade):
        return Crianca(id=id, nome=nome, idade=idade, cpf_responsavel=self.cpf)

    def cria_tarefas(self, id, titulo, capa, descricao, prazo, status, trofeus, id_crianca):
        return Tarefa(id=id, titulo=titulo, capa=capa, descricao=descricao, prazo=prazo, status=status, trofeus=trofeus, id_crianca=id_crianca)

    def exibir_informacoes(self):
        print("CPF:", self.cpf)
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Login:", self.login)
        print("Senha:", self.senha)