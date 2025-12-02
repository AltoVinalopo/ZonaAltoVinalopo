from . import db


class Zona(db.Model):
    __tablename__ = "zonas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=True)
    descripcion = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=True)
