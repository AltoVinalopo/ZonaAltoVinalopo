from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from modelos import db
from modelos.user import User
from auth import auth_bp
from zonas import zonas_bp
from ayuntamientos import aytos_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except:
            return None

    # Crear tablas + crear admin si no existe
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(username="admin").first()
        if not admin:
            admin = User(username="admin", role="ADMIN")
            admin.set_password("admin1234")
            db.session.add(admin)
            db.session.commit()
            print("✔ Usuario admin creado en Render")

    # Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(zonas_bp)
    app.register_blueprint(aytos_bp, url_prefix="/ayuntamientos")

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run()


