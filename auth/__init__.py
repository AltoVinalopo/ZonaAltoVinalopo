from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Carga las rutas del módulo actual
from . import routes
