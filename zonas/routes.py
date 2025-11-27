# zonas/routes.py
from flask import render_template, abort
from flask_login import login_required, current_user

from . import zonas_bp
from modelos.zona import Zona


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
def detalle(zona_id: int):
    """
    Detalle de una zona concreta.
    En la vista mostramos la web propia de esa zona embebida en un iframe.
    """
    zona = Zona.query.get_or_404(zona_id)

    if not zona.url:
        abort(404)

    return render_template(
        "zona_detalle.html",
        usuario=current_user,
        zona=zona,
    )
