from src.entities.tarefa import Tarefa


class Crianca:
    def __init__(self, id, nome, idade, trofeus, cpf_responsavel):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.trofeus = trofeus
        self.cpf_responsavel = cpf_responsavel
        self.tarefas_concluidas = []
        self.livros_concluidos = []

    def iniciar_tarefa(self, id_tarefa):
        tarefa = Tarefa(id=id_tarefa, status="INICIADO", id_crianca=self.id)
        return tarefa.exibir_informacoes()

    def iniciar_livro(self, id_livro):
        livro = Tarefa(id=id_livro, status="INICIADO", id_crianca=self.id)
        return livro.exibir_informacoes()

    def concluir_tarefa(self, id_tarefa):
        self.tarefas_concluidas.append(id_tarefa)

    def concluir_livro(self, id_livro):
        self.livros_concluidos.append(id_livro)

    def listar_tarefas_concluidas(self):
        if len(self.tarefas_concluidas) == 0:
            print(f"{self.nome} não concluiu nenhuma tarefa.")
        else:
            print(f"Tarefas concluídas por {self.nome}:")
            for tarefa in self.tarefas_concluidas:
                print("- " + tarefa)

    def listar_livros_concluidos(self):
        if len(self.livros_concluidos) == 0:
            print(f"{self.nome} não concluiu nenhuma tarefa.")
        else:
            print(f"Tarefas concluídas por {self.nome}:")
            for livro in self.livros_concluidos:
                print("- " + livro)

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Pontuação:", self.trofeus)
        print("CPF do Responsável:", self.cpf_responsavel)