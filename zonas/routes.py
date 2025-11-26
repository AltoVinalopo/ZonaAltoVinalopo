from flask import render_template
from flask_login import login_required, current_user
from . import zonas_bp

ZONAS = [
    {"id": 1, "nombre": "Zona 1 - Alacantí"},
    {"id": 2, "nombre": "Zona 2 - Alto Vinalopó"},
    {"id": 3, "nombre": "Zona 3 - Bajo Vinalopó"},
    {"id": 4, "nombre": "Zona 4 - Alcoi"},
    {"id": 5, "nombre": "Zona 5 - Marina Alta"},
    {"id": 6, "nombre": "Zona 6 - Marina Baja"},
    {"id": 7, "nombre": "Zona 7 - Elche"},
    {"id": 8, "nombre": "Zona 8 - Vega Baja"},
]

@zonas_bp.route("/")
@login_required
def index():
    return render_template("zonas.html", zonas=ZONAS, usuario=current_user)
