from flask import render_template
from flask_login import login_required, current_user
from modelos.iniciativa import Iniciativa
from . import aytos_bp


@aytos_bp.route("/panel")
@login_required
def panel():
    return render_template("panel.html", usuario=current_user)


@aytos_bp.route("/")
@login_required
def listado_iniciativas():
    iniciativas = Iniciativa.query.order_by(Iniciativa.created_at.desc()).all()
    return render_template(
        "ayuntamientos/index.html",
        usuario=current_user,
        iniciativas=iniciativas,
    )
