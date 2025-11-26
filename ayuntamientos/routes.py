from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from modelos.roles import ROLES
from modelos.ayuntamiento import Ayuntamiento

aytos_bp = Blueprint("aytos", __name__)


@aytos_bp.route("/ayuntamientos")
@login_required
def lista_ayuntamientos():
    if current_user.role not in (ROLES["ADMIN_GENERAL"], ROLES["ADMIN_ZONA"]):
        flash("No tienes permisos para acceder a esta sección", "danger")
        return redirect(url_for("panel"))

    ayuntamientos = Ayuntamiento.query.all()
    return render_template("ayuntamientos/lista.html", ayuntamientos=ayuntamientos)


@aytos_bp.route("/ayuntamientos/<int:id>")
@login_required
def detalle_ayuntamiento(id):
    ayto = Ayuntamiento.query.get_or_404(id)
    return render_template("ayuntamientos/detalle.html", ayuntamiento=ayto)
