from ..extensions import db
from ..association import association_table
from app.Turmas.model import Turmas

class Alunos(db.Model): 
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    cpf = db.Column(db.Integer, nullable = False, unique = True)
    data_nascimento = db.Column(db.Integer, nullable = False)
    sexo = db.Column(db.String(20), nullable = False)
    periodo_ingresso = db.Column(db.Integer, nullable = False)
    curso = db.Column(db.String(50), nullable = False) 

    materias_id = db.Column(db.Integer, db.foreignKey('materias.id'))

    professores = db.relationship('Professores', secondary = association_table, backref= 'alunos')

    boletim_id = db.Column(db.Integer, db.ForeignKey('boletim.id'))
    boletim = db.relationship(Boletim, back_populates = "alunos")

    turmas = db.relationship(Turmas, backref = 'turmas')





