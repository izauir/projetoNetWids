class Responsavel:
    def __init__(self, cpf, nome, endereco, login, senha):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.login = login
        self.senha = senha

    def exibir_informacoes(self):
        print("CPF:", self.cpf)
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Login:", self.login)
        print("Senha:", self.senha)