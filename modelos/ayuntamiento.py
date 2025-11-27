# modelos/ayuntamiento.py
from modelos import db


class Ayuntamiento(db.Model):
    __tablename__ = "ayuntamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    municipio = db.Column(db.String(100), nullable=False)

    # Usuarios ligados a este ayuntamiento (concejal, etc.)
    usuarios = db.relationship("User", backref="ayuntamiento", lazy=True)

    # Iniciativas que pertenecen a este ayuntamiento
    iniciativas = db.relationship("Iniciativa", backref="ayuntamiento", lazy=True)
