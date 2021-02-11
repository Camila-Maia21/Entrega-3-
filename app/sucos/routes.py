from flask import Blueprint
from .controllers import (SucosDetails, PaginaSucos)

sucos_api = Blueprint('sucos_api', __name__)

sucos_api.add_url_rule(
    '/sucos', view_func = SucosDetails.as_view('sucos_details'), methods = ['GET', 'POST']
)

sucos_api.add_url_rule(
    '/sucos/<int:id>', view_func = PaginaSucos.as_view('pagina_sucos'), methods = ['GET', 'PATCH']
)
