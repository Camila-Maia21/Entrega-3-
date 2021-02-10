from flask import request, Blueprint, jsonify  
from app.extensions import db 

bebidas_api  = Blueprint ('bebidas_api', __name__)

@bebidas_api.route('/bebidas', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        bebidas = Bebidas.query.all()
        return jsonify(bebida.json() for bebida in bebidas), 200

 
    if request.method == 'POST':
        dados = request.json

        suco = data.get('suco')
        refrigerante = data.get ('refrigerante')
        agua = data.get ('agua')
        alcool = data.get ('alcool')

        if not isinstance(suco, str) or not isinstance(refrigerante, str) or not isinstance(agua, str) or not isinstance(alcool, str):
            return {"error" : "Algum tipo invalido"}, 400

        bebidas = Bebidas (suco = suco, refrigerante =  refrigerante, agua = agua, alcool = alcool)

        db.session.add(bebidas)
        db.session.commit()

        return bebidas.json(), 200

@bebidas_api.route('/bebidas/<int:id>', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def pagina_bebidas(id):
    bebidas = Bebidas.query.get_or_404(id)

    if request.method == 'GET':
        return bebidas.json(), 200

    if request.method == 'PATCH':
        dados = request.json

        suco = data.get('suco', bebidas.suco)
        refrigerante = data.get ('refrigerante', bebidas.refrigerante)
        agua = data.get ('agua', bebidas.agua)
        alcool = data.get ('alcool', bebidas.alcool)

    if not isinstance(suco, str) or not isinstance(refrigerante, str) or not isinstance(agua, str) or not isinstance(alcool, str):
            return {'error' : 'tipo errado'}, 400

        
    bebidas.suco = suco
    bebidas.refrigerante = refrigerante
    bebidas.agua = agua
    bebidas.alcool = alcool

    db.session.commit()


   
