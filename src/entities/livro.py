class Livro:
    def __init__(self, id, titulo, capa, idioma, descricao, prazo, status, trofeu, recompensa, tipo, id_crianca, id_jornada):
        self.id = id
        self.titulo = titulo
        self.capa = capa
        self.idioma = idioma
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        self.trofeu = trofeu
        self.recompensa = recompensa
        self.tipo = tipo
        self.id_crianca = id_crianca
        self.id_jornada = id_jornada

    def exibir_informacoes(self):
        print("ID: ", self.id)
        print("Título: ", self.titulo)
        print("Capa: ", self.capa)
        print("Idioma: ", self.idioma)
        print("Descrição: ", self.descricao)
        print("Prazo: ", self.prazo)
        print("Status: ", self.status)
        print("Trofeus: ", self.trofeu)
        print("Recompensas: ", self.recompensa)
        print("Tipo: ", self.tipo)
        print("ID da Criança: ", self.id_crianca)
        print("ID da Jornada: ", self.id_jornada)