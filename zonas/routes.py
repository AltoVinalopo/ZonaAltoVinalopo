# zonas/routes.py
from flask import render_template, abort
from flask_login import login_required, current_user

from modelos.zona import Zona
from . import zonas_bp


@zonas_bp.route("/")
@login_required
def index():
    """
    Listado de zonas para el panel principal.
    """
    zonas = Zona.query.order_by(Zona.id).all()
    return render_template(
        "zonas_index.html",
        usuario=current_user,
        zonas=zonas,
    )

@zonas_bp.route("/<int:zona_id>/")
@login_required
def zona_detalle(zona_id):
    zona = Zona.query.get_or_404(zona_id)
    return render_template("zona_detalle.html", zona=zona)


