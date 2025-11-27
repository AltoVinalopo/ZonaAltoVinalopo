# modelos/zona.py
from modelos import db


class Zona(db.Model):
    __tablename__ = "zonas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(255), nullable=True)
