# ayuntamientos/routes.py
from flask import render_template
from flask_login import login_required, current_user

from . import aytos_bp


@aytos_bp.route("/panel")
@login_required
def panel():
    """
    Panel principal: muestra las opciones 'Zonas y municipios'
    y 'Ayuntamientos'.
    """
    return render_template(
        "panel.html",
        usuario=current_user,
    )

