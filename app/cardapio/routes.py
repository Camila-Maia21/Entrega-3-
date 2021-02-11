from flask import Blueprint
from .controllers import (CardapioDetails, PaginaCardapio)

cardapio_api = Blueprint('cardapio_api', __name__)

cardapio_api.add_url_rule(
    '/cardapio', view_func = CardapioDetails.as_view('cardapio_details'), methods = ['GET', 'POST']
)

cardapio_api.add_url_rule(
    '/cardapio/<int:id>', view_func = PaginaCardapio.as_view('pagina_cardapio'), methods = ['GET', 'PATCH']
)
