from ..extensions import db
from app.Materias.model import Materias

class Turmas(db.Model): 
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key = True)
    horario = db.Column(db.Integer, nullable = False)

    materias = db.relationship(Materias, uselist = False, back_populates="turmas")

    alunos_id = db.Column(db.Integer, db.ForeignKey('alunos.id'))

    professores_id = db.Column(db.Integer, db.ForeignKey('professores.id'))



