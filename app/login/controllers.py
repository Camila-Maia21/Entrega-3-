from flask import request, Blueprint, jsonify  
from flask.views import MethodView
from app.login.model import Login
from app.extensions import db 
import bcrypt

#login_api = Blueprint('login_api', __name__)

class LoginDetails(MethodView): #login
    def get(self):
        login = Login.query.all()
        return jsonify(login.json() for login in login), 200


    def post(self):
        data = request.json

        nome = data.get('nome')
        email = data.get('email')
        senha = str(data.get('senha'))

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.genslat())

        login = Login(nome = nome, email =  email, senha_hash = senha_hash)

        db.session.add(login)
        db.session.commit()

        return bebidas.json(), 200

class PaginaLogin(MethodView): #/login/<int:id>
    def get(self, id):
        login = Login.query.get_or_404(id)
        return login.json(), 200


    def patch(self, id):
        login = Login.query.get_or_404(id)
        data = request.json

        nome = data.get('nome', login.nome)
        email = data.get('email', login.email)
        senha = data.get('senha', login.senha)

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400

        
        login.nome = nome
        login.email = email
        login.senha = senha

        db.session.commit()




