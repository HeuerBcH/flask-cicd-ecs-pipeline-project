from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

tarefa_responsaveis = db.Table('tarefa_responsaveis',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True),
    db.Column('tarefa_id', db.Integer, db.ForeignKey('tarefas.id'), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    empresa = db.Column(db.String(45), nullable=True)
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Relacionament pra Tarefas onde o Usuário é Responsável
    tarefas = db.relationship(
        'Tarefa',
        secondary = 'tarefa_responsaveis',
        back_populates = 'responsaveis'
    )

    def __repr__(self):
        return f'<Usuario {self.username}>'

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    prioridade = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pendente')
    prazo = db.Column(db.Date, nullable=True)
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    criado_por = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # Relacionamento dos Responsáveis
    responsaveis = db.relationship(
        'Usuario',
        secondary = 'tarefa_responsaveis',
        back_populates = 'tarefas'
    )

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'

