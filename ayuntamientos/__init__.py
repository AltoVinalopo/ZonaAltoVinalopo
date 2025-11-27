# ayuntamientos/__init__.py
from flask import Blueprint

aytos_bp = Blueprint("ayuntamientos", __name__, url_prefix="/ayuntamientos")

from . import routes  # noqa
