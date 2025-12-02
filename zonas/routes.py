from flask import render_template
from flask_login import login_required, current_user
from modelos.zona import Zona
from . import zonas_bp


@zonas_bp.route("/")
@login_required
def index():
    zonas = Zona.query.order_by(Zona.nombre.asc()).all()
    return render_template(
        "zonas/index.html",
        usuario=current_user,
        zonas=zonas,
    )
