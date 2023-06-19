class Tarefa:
    def __init__(self, id, titulo, capa, descricao, prazo, status, trofeus, id_crianca):
        self.id = id
        self.titulo = titulo
        self.capa = capa
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        self.trofeus = trofeus
        self.id_crianca = id_crianca

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Imagem:", self.capa)
        print("Descrição:", self.descricao)
        print("Prazo:", self.prazo)
        print("Status:", self.status)
        print("trofeus:", self.trofeus)
        print("ID da Criança:", self.id_crianca)