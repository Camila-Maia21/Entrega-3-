from flask import Blueprint
from .controllers import (BebidasDetails, PaginaBebidas)

bebidas_api = Blueprint('bebidas_api', __name__)

bebidas_api.add_url_rule(
    '/bebidas', view_func = BebidasDetails.as_view('bebidas_details'), methods = ['GET', 'POST']
)

bebidas_api.add_url_rule(
    '/bebidas/<int:id>', view_func = PaginaBebidas.as_view('pagina_bebidas'), methods = ['GET', 'PATCH']
)


