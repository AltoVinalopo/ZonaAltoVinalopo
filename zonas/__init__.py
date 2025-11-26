# zonas/__init__.py
from flask import Blueprint

zonas_bp = Blueprint("zonas", __name__, url_prefix="/zonas")

from . import routes  # noqa: E402,F401
