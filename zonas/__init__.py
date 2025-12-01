# zonas/__init__.py
from flask import Blueprint

# El blueprint se registra con el nombre correcto "zonas"
zonas_bp = Blueprint(
    "zonas",
    __name__,
    url_prefix="/zonas"
)

from . import routes
