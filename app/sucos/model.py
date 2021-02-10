from ..extensions import db
from ..association import association_table

class Sucos(db.Model): 
    __tablename__ = 'sucos'
    id = db.Column(db.Integer, primary_key = True)
    abacaxi_hortela = db.Column(db.String(50), nullable = False)
    batata_doce = db.Column(db.String(50), nullable = False)
    detox = db.Column(db.String(50), nullable = False)
    laranja = db.Column(db.String(50), nullable = False)

    bebidas = db.relationship('Bebidas', secondary = association_table, backref= 'suco')

    def json(self): 
        return {
            "abacaxi_hortela": self.abacaxi_hortela,
            "batata_doce": self.batata_doce,
            "detox": self.detox,
            "laranja": self.laranja

        }

