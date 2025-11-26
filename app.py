# app.py
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from modelos import db

login_manager = LoginManager()
login_manager.login_view = "auth.login"   # endpoint del login


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Importar aquí para evitar imports circulares
    from modelos.user import User

    # === Flask-Login: user_loader OBLIGATORIO ===
    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    # Registrar blueprints
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)

    # Ruta raíz -> al login (o al panel si ya está logueado)
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # Crear tablas + usuario admin si no existe
    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username="admin").first():
            admin = User(
                username="admin",
                role="ADMIN_GENERAL",   # este verá TODO
            )
            admin.set_password("admin1234")
            db.session.add(admin)
            db.session.commit()
            print(">>> Usuario admin creado automáticamente")

    return app


# Instancia global que usará gunicorn
app = create_app()


