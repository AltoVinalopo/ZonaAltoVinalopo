from ..app import db

class Ayuntamiento(db.Model):
    __tablename__ = "ayuntamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)

    iniciativas = db.relationship("Iniciativa", backref="ayuntamiento", lazy=True)
