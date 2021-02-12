from flask import request, jsonify, render_template  
from flask.views import MethodView
from app.login.model import Login
from app.extensions import db, mail 
import bcrypt
from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


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

        msg = Message (sender='camilamaia@poli.ufrj.br',
                       recipients=[email],
                       subject='Bem-vindo!',
                       html=render_template('email.html', nome= nome))

        mail.send(msg)

        return login.json(), 200

class PaginaLogin(MethodView): #/login/<int:id>

    decorators = [jwt_required]

    def get(self, id):
        if get_jwt_identity() != id:
            return {"error": "Usuario não permitido"}, 400
        login = Login.query.get_or_404(id)
        return login.json(), 200


    def patch(self, id):
        if get_jwt_identity() != id:
            return {"error": "Usuario não permitido"}, 400
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


class UsuarioLogin(MethodView): #usuariologin
    def post(self): 
        data = request.json

        email = data.get('email')
        senha = str(data.get('senha'))

        login = Login.query.filter_by(email= email).first()

        if not login or not bcrypt.checkpw(senha.encode(), login.senha_hash):
            return{"error": "Usuario não encontrado"}, 400


        token = create_access_token(identity=login.id)
        
        return {"token": token}, 200











