from flask import Blueprint

aytos_bp = Blueprint('aytos', __name__, url_prefix='/ayuntamientos')
from . import routes
