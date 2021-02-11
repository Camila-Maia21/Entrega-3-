from flask import request, Blueprint, jsonify
from flask.views import MethodView
from app.cardapio.model import Cardapio 
from app.extensions import db 


class CardapioDetails(MethodView): #cardapio
    def get(self):
        cardapio = Cardapio.query.all()
        return jsonify(cardapio.json() for cardapio in cardapio), 200

    def post(self):
        data = request.json

        bebidas = data.get('bebidas')
        petiscos = data.get('petiscos')
        doces = data.get('doces')

        if not isinstance(bebidas, str) or not isinstance(petiscos, str) or not isinstance(doces, str):
            return {"error" : "Algum tipo invalido"}, 400

        cardapio = Cardapio(bebidas = bebidas, pesticos =  pestiscos, doces = doces)

        db.session.add(cardapio)
        db.session.commit()

        return cardapio.json(), 200

class PaginaCardapio(MethodView): #/cardapio/<int:id>
    def get(self, id): 
        cardapio = Cardapio.query.get_or_404(id)
        return cardapio.json(), 200

    def patch(self, id):
        cardapio = Cardapio.query.get_or_404(id)
        data = request.json

        bebidas = data.get('bebidas', cardapio.bebidas)
        petiscos = data.get('petiscos', cardapio.pestiscos)
        doces = data.get('doces', cardapio.doces)

        if not isinstance(bebidas, str) or not isinstance(petiscos, str) or not isinstance(doces, str):
            return {"error" : "Algum tipo invalido"}, 400

        cardapio.bebidas = bebidas
        cardapio.pestiscos = petiscos
        cardapio.doces = doces

        db.session.commit()
