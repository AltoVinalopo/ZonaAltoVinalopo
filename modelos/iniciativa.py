# modelos/iniciativa.py
from datetime import datetime
from modelos import db


class Iniciativa(db.Model):
    __tablename__ = "iniciativas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(40), default="Pendiente")
    fecha_pleno = db.Column(db.Date, nullable=True)
    pdf_path = db.Column(db.String(255), nullable=True)
    concejal_nombre = db.Column(db.String(120), nullable=True)

    ayuntamiento_id = db.Column(
        db.Integer,
        db.ForeignKey("ayuntamientos.id"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

