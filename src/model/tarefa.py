class Tarefa:
    def __init__(self, id, titulo, img, descricao, prazo, status, pontos, id_crianca):
        self.id = id
        self.titulo = titulo
        self.img = img
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        self.pontos = pontos
        self.id_crianca = id_crianca

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Imagem:", self.img)
        print("Descrição:", self.descricao)
        print("Prazo:", self.prazo)
        print("Status:", self.status)
        print("Pontos:", self.pontos)
        print("ID da Criança:", self.id_crianca)