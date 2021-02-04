from ..extensions import db
from app.Alunos.model import Alunos

class Materias(db.Model): 
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    codigo = db.Column(db.Integer, nullable = False, unique = True)

    alunos = db.relationship(Alunos, backref = 'alunos')

    professores_id = db.Column(db.Integer, db.foreignKey('professores.id'))

    tumas_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    turmas = db.relationship(Turmas, back_populates="materias")

    

