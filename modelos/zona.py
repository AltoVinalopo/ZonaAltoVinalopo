from modelos import db

class Zona(db.Model):
    __tablename__ = "zonas"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    ayuntamiento_id = db.Column(db.Integer, db.ForeignKey("ayuntamientos.id"), nullable=False)

    usuarios = db.relationship("User", backref="zona", lazy=True)
