from . import db


class Ayuntamiento(db.Model):
    __tablename__ = "ayuntamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    municipio = db.Column(db.String(100), nullable=False)

    usuarios = db.relationship("User", backref="ayuntamiento", lazy=True)
    iniciativas = db.relationship("Iniciativa", backref="ayuntamiento", lazy=True)
