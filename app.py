# app.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from modelos import db

# =========================
# LOGIN MANAGER
# =========================
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Importar aquí para evitar imports circulares
    from modelos.user import User
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp
    from zonas import zonas_bp       # <-- OK

    # Flask-Login loader
    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)
    app.register_blueprint(zonas_bp)

    # Ruta raíz
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # =====================================
    # CREAR TABLAS + USUARIO ADMIN
    # =====================================
    with app.app_context():
        db.create_all()

        # Usuario admin
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


# Instancia global usada por Render/Gunicorn
app = create_app()

