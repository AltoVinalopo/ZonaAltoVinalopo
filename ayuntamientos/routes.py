# ayuntamientos/routes.py
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

# CARGAMOS CORRECTAMENTE EL BLUEPRINT
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
        usuario=current_user
    )
