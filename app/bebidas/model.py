from ..extensions import db
from ..association import association_table

class Bebidas(db.Model): 
    __tablename__ = 'bebidas'
    id = db.Column(db.Integer, primary_key = True)
    sucos = db.Column(db.String(50), nullable = False)
    refrigerantes = db.Column(db.String(20), nullable = False) 
    agua = db.Column(db.String(20), nullable = False) 
    alcool = db.Column(db.String(20), nullable = False) 


    sucos = db.relationship('Sucos', secondary = association_table, backref= 'bebida')

    cardapio_id = db.Column(db.Integer, db.ForeignKey('cardapio.id'))

    def json(self): 
        return {
            "sucos": self.sucos,
            "refrigerantes": self.refrigerantes,
            "agua": self.agua,
            "alcool": self.alcool
        }



