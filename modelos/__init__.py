# modelos/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = ["db"]
