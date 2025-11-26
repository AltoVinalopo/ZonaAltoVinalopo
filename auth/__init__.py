# modelos/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Instancia global de la BBDD
db = SQLAlchemy()

# Importa los modelos para que SQLAlchemy los conozca
from .user import User          # noqa: F401
from .ayuntamiento import Ayuntamiento  # noqa: F401
from .zona import Zona          # noqa: F401
# añade aquí más modelos si los tienes
