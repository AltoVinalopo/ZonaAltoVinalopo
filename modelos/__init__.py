# modelos/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# importa los modelos para que se creen las tablas con create_all()
from .user import User          # noqa
from .ayuntamiento import Ayuntamiento  # noqa
from .zona import Zona          # noqa
from .iniciativa import Iniciativa  # noqa
