from flask import request, Blueprint, jsonify  
from app.extensions import db 

bebidas_api  = Blueprint ('bebidas_api', __name__)

@bebidas_api.route('/bebidas', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        bebidas = Bebidas.query.all()
        return jsonify(bebida.json() for bebida in bebidas), 200

 
    if request.method == 'POST':
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

@bebidas_api.route('/bebidas/<int:id>', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def pagina_bebidas(id):
    bebidas = Bebidas.query.get_or_404(id)

    if request.method == 'GET':
        return bebidas.json(), 200

    if request.method == 'PATCH':
        data = request.json

        sucos = data.get('sucos', bebidas.sucos)
        refrigerantes = data.get('refrigerantes', bebidas.refrigerantes)
        agua = data.get('agua', bebidas.agua)
        alcool = data.get('alcool', bebidas.alcool)

    if not isinstance(sucos, str) or not isinstance(refrigerantes, str) or not isinstance(agua, str) or not isinstance(alcool, str):
            return {'error' : 'tipo errado'}, 400

        
    bebidas.sucos = sucos
    bebidas.refrigerantes = refrigerantes
    bebidas.agua = agua
    bebidas.alcool = alcool

    db.session.commit()


   
