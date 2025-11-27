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
def detalle_zona(zona_id: int):
    """
    Detalle de una zona concreta.
    Aquí mostramos un botón grande que abre el proyecto
    externo de esa zona (campo Zona.url).
    """
    zona = Zona.query.get(zona_id)
    if not zona:
        abort(404)

    return render_template(
        "zona_detalle.html",
        usuario=current_user,
        zona=zona,
    )

