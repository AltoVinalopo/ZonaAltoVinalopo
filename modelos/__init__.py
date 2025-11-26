# modelos/__init__.py
from flask_sqlalchemy import SQLAlchemy

# 1. Crear instancia global de SQLAlchemy
db = SQLAlchemy()

# 2. Importar modelos (solo DESPUÉS de crear db)
from .user import User        # noqa: F401
from .ayuntamiento import Ayuntamiento  # noqa: F401
from .zona import Zona        # noqa: F401
