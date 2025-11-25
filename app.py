from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from modelos.user import User  # noqa: F401

    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp
    from zonas.routes import zonas_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)
    app.register_blueprint(zonas_bp)

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("panel"))
        return redirect(url_for("auth.login"))

    from flask import render_template
    from modelos.roles import ROLES

    @app.route("/panel")
    def panel():
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        return render_template("panel.html", user=current_user, ROLES=ROLES)

    return app

app = create_app()
if __name__ == "__main__":
    app.run()
