from modelos import db

class Ayuntamiento(db.Model):
    __tablename__ = "ayuntamientos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    municipio = db.Column(db.String(100), nullable=False)

    zonas = db.relationship("Zona", backref="ayuntamiento", lazy=True)
    usuarios = db.relationship("User", backref="ayuntamiento", lazy=True)
