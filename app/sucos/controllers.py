from flask import request, Blueprint, jsonify  
from app.extensions import db 

sucos_api  = Blueprint ('sucos_api', __name__)

@sucos_api.route('/sucos', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        sucos = Sucos.query.all()
        return jsonify(suco.json() for suco in sucos), 200

    if request.method == 'POST':
        data = request.json

        abacaxi_hortela = data.get('abacaxi_hortela')
        batata_doce = data.get('batata_doce')
        detox = data.get('detox')
        laranja = data.get('laranja')

        if not isinstance(abacaxi_hortela, str) or not isinstance(batata_doce, str) or not isinstance(detox, str) or not isinstance(laranja, str):
            return {"error" : "Algum tipo invalido"}, 400

        sucos = Sucos(abacaxi_hortela = abacaxi_hortela, batata_doce =  batata_doce, detox = detox, laranja = laranja)

        db.session.add(sucos)
        db.session.commit()

        return sucos.json(), 200

@sucos_api.route('/sucos/<int:id>', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def pagina_sucos(id):
    sucos = Sucos.query.get_or_404(id)

    if request.method == 'GET':
        return sucos.json(), 200

    if request.method == 'PATCH':
        data = request.json

        abacaxi_hortela = data.get('abacaxi_hortela', cardapio.abacaxi_hortela)
        batata_doce = data.get('batata_doce', cardapio.batata_doce)
        detox = data.get('detox', cardapio.detox)
        laranja = data.get('laranja', cardapio.laranja)


        if not isinstance(abacaxi_hortela, str) or not isinstance(batata_doce, str) or not isinstance(detox, str) or not isinstance(laranja, str):
            return {"error" : "Algum tipo invalido"}, 400


        cardapio.abacaxi_hortela = abacaxi_hortela
        cardapio.batata_doce = batata_doce
        cardapio.detox = detox
        cardapio.laranja = laranja

        db.session.commit()


        


