# app.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from modelos import db
from zonas import zonas_bp
app.register_blueprint(zonas_bp)

login_manager = LoginManager()
login_manager.login_view = "auth.login"   # endpoint del login


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Importar modelos aquí (evita import circular)
    from modelos.user import User

    # === Flask-Login: CARGA DEL USUARIO ===
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # === REGISTRO DE BLUEPRINTS ===
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp
    from zonas import zonas_bp   # <<--- añadido

    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)
    app.register_blueprint(zonas_bp)  # <<--- añadido

    # === RUTA PRINCIPAL ===
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # === CREACIÓN DE TABLAS Y ADMIN ===
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username="admin").first():
            admin = User(
                username="admin",
                role="ADMIN_GENERAL"
            )
            admin.set_password("admin1234")
            db.session.add(admin)
            db.session.commit()
            print(">>> Usuario admin creado automáticamente")

    return app


# Instancia global usada por gunicorn
app = create_app()


