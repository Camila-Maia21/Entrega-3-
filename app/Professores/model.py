from ..extensions import db
from ..association import association_table
from app.Materias.model import Materias
from app.Turmas.model import Turmas

class Professores(db.Model): 
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    cpf = db.Column(db.Integer, nullable = False, unique = True)
    formacao = db.Column(db.String(50), nullable = False)

    alunos = db.relationship('Alunos', secondary = association_table, backref= 'professores')

    materias = db.relationship(Materias, backref = 'materias')
    
    turmas = db.relationship(Turmas, backref = 'turmas')