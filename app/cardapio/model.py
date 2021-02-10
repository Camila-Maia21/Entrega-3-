from ..extensions import db

class Cardapio(db.Model): 
    __tablename__ = 'cardapio'
    id = db.Column(db.Integer, primary_key = True)
    bebidas = db.Column(db.String(50), nullable = False)
    petiscos = db.Column(db.String(50), nullable = False)
    doces = db.Column(db.String(50), nullable = False)

    bebidas = db.relationship('Bebidas', backref = 'cardapio')

    def json(self): 
        return {
            "bebidas": self.bebidas,
            "petiscos": self.petiscos,
            "doces": self.doces
        }



