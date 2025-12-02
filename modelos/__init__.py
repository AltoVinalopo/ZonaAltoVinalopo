from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User          # noqa
from .ayuntamiento import Ayuntamiento  # noqa
from .zona import Zona          # noqa
from .iniciativa import Iniciativa  # noqa
