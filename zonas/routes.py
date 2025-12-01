# zonas/routes.py
from flask import render_template
from flask_login import login_required, current_user

from . import zonas_bp


@zonas_bp.route("/")
@login_required
def index():
    """
    Página principal con todas las zonas y municipios.
    """
    # El backend debe tener la variable zonas cargada.
    # Si antes funcionaba, esto ya existía.
    from modelos.zonas import obtener_todas_las_zonas  # ejemplo
    zonas = obtener_todas_las_zonas()

    return render_template(
        "zonas_index.html",
        usuario=current_user,
        zonas=zonas
    )
