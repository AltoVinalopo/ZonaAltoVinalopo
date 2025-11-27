from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User          # noqa
from .ayuntamiento import Ayuntamiento  # si existe
from .zona import Zona          # noqa
