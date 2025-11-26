from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required

from app import db
from modelos.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash("Usuario o contraseña incorrectos", "danger")
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
@auth_bp.route('/crear-admin')
def crear_admin():
    from modelos.user import User
    from app import db

    # Si ya existe, no lo vuelve a crear
    existing = User.query.filter_by(username="admin").first()
    if existing:
        return "El usuario admin ya existe"

    admin = User(username="admin", role="ADMIN_GENERAL")
    admin.set_password("admin1234")

    db.session.add(admin)
    db.session.commit()

    return "Usuario admin creado correctamente"

