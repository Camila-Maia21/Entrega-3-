from flask import request, Blueprint, jsonify  
from app.extensions import db 

cardapio_api  = Blueprint ('cardapio_api', __name__)

@cardapio_api.route('/cardapio', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        cardapio = Cardapio.query.all()
        return jsonify(cardapio.json() for cardapio in cardapio), 200

    if request.method == 'POST':
        dados = request.json

        bebidas = data.get('bebidas')
        petiscos = data.get ('petiscos')
        doces = data.get ('doces')

        if not isinstance(bebidas, str) or not isinstance(petiscos, str) or not isinstance(doces, str):
            return {"error" : "Algum tipo invalido"}, 400

        cardapio = Cardapio (bebidas = bebidas, pesticos =  pestiscos, doces = doces)

        db.session.add(cardapio)
        db.session.commit()

        return cardapio.json(), 200

@cardapio_api.route('/cardapio/<int:id>', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def pagina_cardapio(id):
    cardapio = Cardapio.query.get_or_404(id)

    if request.method == 'GET':
        return cardapio.json(), 200

    if request.method == 'PATCH':
        dados = request.json

        bebidas = data.get('bebidas', cardapio.bebidas)
        petiscos = data.get ('petiscos', cardapio.pestiscos)
        doces = data.get ('doces', cardapio.doces)

        if not isinstance(bebidas, str) or not isinstance(petiscos, str) or not isinstance(doces, str):
            return {'error' : 'tipo errado'}, 400

        cardapio.bebidas = bebidas
        cardapio.pestiscos = petiscos
        cardapio.doces = doces

        db.session.commit()







