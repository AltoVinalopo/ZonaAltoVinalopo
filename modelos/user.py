from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Roles de ejemplo:
    #  - ADMIN_GENERAL
    #  - COORDINADOR_ZONA
    #  - CONCEJAL
    role = db.Column(db.String(40), nullable=False, default="CONCEJAL")

    zona_id = db.Column(db.Integer, nullable=True)
    ayuntamiento_id = db.Column(db.Integer, db.ForeignKey("ayuntamientos.id"), nullable=True)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def has_role(self, *roles) -> bool:
        return self.role in roles
