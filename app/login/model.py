from ..extensions import db

class Login(db.Model): 
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = True)
    senha_hash = db.Column(db.String(20), nullable = False)  

    def json(self): 
        return {
            "nome": self.nome,
            "email": self.email
        }