class Jornada:
    def __init__(self, id, escolaridade, img, nivel_interpretação, qtd_texto, id_crianca, tipo_letra):
        self.id = id
        self.escolaridade = escolaridade
        self.img = img
        self.nivel_interpretacao = nivel_interpretação
        self.qtd_texto = qtd_texto
        self.tipo_letra = tipo_letra
        self.id_crianca = id_crianca

    def exibir_informacoes(self):
        print("ID: ", self.id)
        print("Escolaridade: ", self.escolaridade)
        print("Imagem: ", self.img)
        print("Nivel interpretação: ", self.nivel_interpretação)
        print("Quantidade de texto:", self.qtd_texto)
        print("Tipo letra:", self.tipo_letra)
        print("ID da Criança:", self.id_crianca)