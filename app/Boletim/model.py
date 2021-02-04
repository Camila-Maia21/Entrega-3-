from ..extensions import db
from app.Alunos.model import Alunos

class Boletim(db.Model): 
    __tablename__ = 'boletim'
    id = db.Column(db.Integer, primary_key = True)
    notas = db.Column(db.Integer, nullable = False)


    alunos = db.relationship(Alunos, uselist = False, back_populates = "boletim")
