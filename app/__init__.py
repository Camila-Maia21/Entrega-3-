from flask import Flask
from .config import Config
from .extensions import db, migrate, mail, jwt

from .bebidas.model import Bebidas
from .cardapio.model import Cardapio
from .sucos.model import Sucos
from .login.model import Login

from app.bebidas.routes import bebidas_api
from app.cardapio.routes import cardapio_api
from app.sucos.routes import sucos_api
from app.login.routes import login_api

from .association import association_table

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(bebidas_api)
    app.register_blueprint(cardapio_api)
    app.register_blueprint(sucos_api)
    app.register_blueprint(login_api)

    return app