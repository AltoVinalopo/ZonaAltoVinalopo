from flask import render_template
from flask_login import login_required, current_user
from . import aytos_bp
from ..modelos.roles import ROLES
from ..modelos.iniciativa import Iniciativa

def _puede_ver_aytos(user):
    return user.role in (
        ROLES["ADMIN_GENERAL"],
        ROLES["ADMIN_AYUNTAMIENTOS"],
        ROLES["ADMIN_VISOR"],
        ROLES["CONCEJAL"],
    )

@aytos_bp.route('/')
@login_required
def index():
    user = current_user
    if not _puede_ver_aytos(user):
        return "No autorizado", 403
    ultimas = Iniciativa.query.order_by(Iniciativa.created_at.desc()).limit(20).all()
    return render_template('ayuntamientos/index.html', iniciativas=ultimas)
