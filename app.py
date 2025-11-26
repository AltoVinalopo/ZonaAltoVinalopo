from flask import Flask
from config import Config
from flask_login import LoginManager
from modelos import db

# Inicializamos LoginManager arriba del todo
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Registrar blueprints (IMPORTANTE: después de init_app)
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)

    # Crear BBDD y usuario admin
    with app.app_context():
        from modelos.user import User   # ← Import seguro, evita circular import

        db.create_all()

        # Crear admin si no existe
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


# Crear la app para gunicorn
app = create_app()


