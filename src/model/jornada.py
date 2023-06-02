class Jornada:
    def __init__(self, id, titulo, img, descricao, id_crianca):
        self.id = id
        self.titulo = titulo
        self.img = img
        self.descricao = descricao
        self.id_crianca = id_crianca

    def exibir_informacoes(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Imagem:", self.img)
        print("Descrição:", self.descricao)
        print("ID da Criança:", self.id_crianca)