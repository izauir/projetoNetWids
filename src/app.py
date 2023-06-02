from flask import Flask
from src.controller.configs_controller import ConfigsController
from src.controller.crianca_controller import CriancaController
from src.controller.jornada_controller import JornadaController
from src.controller.livros_controller import LivrosController
from src.controller.responsavel_controller import ResponsavelController

app = Flask(__name__)

app.register_blueprint(ConfigsController)
app.register_blueprint(CriancaController)
app.register_blueprint(JornadaController)
app.register_blueprint(LivrosController)
app.register_blueprint(ResponsavelController)

if __name__ == '__main__':
    app.run()