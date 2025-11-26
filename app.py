from flask import Flask, redirect, url_for
from config import Config
from flask_login import LoginManager
from modelos import db

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Registrar blueprints
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)

    # Ruta raíz -> redirige a login
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # Crear tablas + usuario admin
    with app.app_context():
        from modelos.user import User
        db.create_all()

        if not User.query.filter_by(username="admin").first():
            admin = User(username="admin", role="ADMIN_GENERAL")
            admin.set_password("admin1234")
            db.session.add(admin)
            db.session.commit()
            print(">>> Usuario admin creado automáticamente")

    return app


# Crear instancia de la app para Gunicorn
app = create_app()

