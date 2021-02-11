from flask import request, Blueprint, jsonify  
from flask.views import MethodView
from app.bebidas.model import Bebidas
from app.extensions import db 


class BebidasDetails(MethodView): #bebidas
    def get(self):
        bebidas = Bebidas.query.all()
        return jsonify(bebida.json() for bebida in bebidas), 200

    def post(self):
        data = request.json

        sucos = data.get('sucos')
        refrigerantes = data.get('refrigerantes')
        agua = data.get('agua')
        alcool = data.get('alcool')

        print(refrigerantes)
        print(sucos)
        print(agua)
        print(alcool)

        if not isinstance(sucos, str) or not isinstance(refrigerantes, str) or not isinstance(agua, str) or not isinstance(alcool, str):
            return {"error" : "Algum tipo invalido"}, 400

        bebidas = Bebidas(sucos = sucos, refrigerantes =  refrigerantes, agua = agua, alcool = alcool)

        db.session.add(bebidas)
        db.session.commit()

        return bebidas.json(), 200

class PaginaBebidas(MethodView): #/bebidas/<int:id>
    def get(self, id):
        bebidas = Bebidas.query.get_or_404(id)
        return bebidas.json(), 200

    def patch(self, id): 
        bebidas = Bebidas.query.get_or_404(id)
        data = request.json

        sucos = data.get('sucos', bebidas.sucos)
        refrigerantes = data.get('refrigerantes', bebidas.refrigerantes)
        agua = data.get('agua', bebidas.agua)
        alcool = data.get('alcool', bebidas.alcool)

        if not isinstance(sucos, str) or not isinstance(refrigerantes, str) or not isinstance(agua, str) or not isinstance(alcool, str):
            return {"error" : "Algum tipo invalido"}, 400

        
        bebidas.sucos = sucos
        bebidas.refrigerantes = refrigerantes
        bebidas.agua = agua
        bebidas.alcool = alcool

        db.session.commit()  
