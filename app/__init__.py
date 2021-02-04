from flask import Flask
from .config import Config
from .extensions import db

from .association import association_table
from app.Alunos.model import Alunos
from app.Boletim.model import Boletim
from app.Materiais.model import Materiais
from app.Professores.model import Professores
from app.Turmas.model import Turmas

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app