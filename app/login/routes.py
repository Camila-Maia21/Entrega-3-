from flask import Blueprint
from .controllers import (LoginDetails, PaginaLogin, UsuarioLogin)

login_api = Blueprint('login_api', __name__)

login_api.add_url_rule(
    '/login', view_func= LoginDetails.as_view('login_details'), methods = ['GET', 'POST']
)

login_api.add_url_rule(
    '/login/<int:id>', view_func= PaginaLogin.as_view('pagina_login'), methods = ['GET', 'PATCH']
)

login_api.add_url_rule(
    '/usuariologin', view_func= UsuarioLogin.as_view('usuario_login'), methods = ['POST']
)


