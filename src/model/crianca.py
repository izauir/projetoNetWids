class Crianca:
    def __init__(self, id, nome, idade, pontuacao, senha, cpf_responsavel):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao
        self.senha = senha
        self.cpf_responsavel = cpf_responsavel

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Pontuação:", self.pontuacao)
        print("Senha:", self.senha)
        print("CPF do Responsável:", self.cpf_responsavel)