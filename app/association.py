from .extensions import db

association_table = db.Table('association', db.Model.metadata,
                             db.Column('bebidas', db.Integer, db.ForeignKey('bebidas.id')),
                             db.Column('sucos', db.Integer, db.ForeignKey('sucos.id')))