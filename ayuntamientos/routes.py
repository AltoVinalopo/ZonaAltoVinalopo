# ayuntamientos/routes.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from modelos import db
from modelos.ayuntamiento import Ayuntamiento
from modelos.zona import Zona

aytos_bp = Blueprint("aytos", __name__)


@aytos_bp.route("/panel")
@login_required
def panel():
    """Panel principal filtrando por rol y zona/ayuntamiento del usuario."""

    if current_user.role == "ADMIN_GENERAL":
        zonas = Zona.query.order_by(Zona.nombre).all()
        aytos = Ayuntamiento.query.order_by(Ayuntamiento.nombre).all()

    elif current_user.role == "COORDINADOR_ZONA" and current_user.zona_id:
        zonas = Zona.query.filter_by(id=current_user.zona_id).all()
        aytos = Ayuntamiento.query.filter_by(zona_id=current_user.zona_id).order_by(
            Ayuntamiento.nombre
        ).all()

    else:  # CONCEJAL u otros roles
        zonas = []
        if current_user.ayuntamiento_id:
            ayto = Ayuntamiento.query.get(current_user.ayuntamiento_id)
            aytos = [ayto] if ayto else []
        else:
            aytos = []

    return render_template(
        "panel.html",
        zonas=zonas,
        ayuntamientos=aytos,
        usuario=current_user,
    )

