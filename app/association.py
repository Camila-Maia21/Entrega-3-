from .extensions import db

association_table = db.Table('association', db.Model.metadata,
                             db.Column('alunos', db.Integer, db.ForeignKey('alunos.id')),
                             db.Column('professores', db.Integer, db.ForeignKey('professores.id')))