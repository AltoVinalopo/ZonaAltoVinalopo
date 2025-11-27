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
    from modelos.zona import Zona
    from auth.routes import auth_bp
    from ayuntamientos.routes import aytos_bp
    from zonas import zonas_bp

    # === Flask-Login: user_loader ===
    @login_manager.user_loader
    def load_user(user_id: str):
        try:
            return User.query.get(int(user_id))
        except (TypeError, ValueError):
            return None

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(aytos_bp)
    app.register_blueprint(zonas_bp)

    # Ruta raíz -> al login
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # Crear tablas + seed de zonas y admin
    with app.app_context():
        db.create_all()

        # --- ZONAS en BBDD (id fijo + URL de cada app) ---
        ZONAS_DEF = [
            (1, "Zona 1 · Alacantí",        "https://coordinacionalacanti.onrender.com/"),
            (2, "Zona 2 · Alto Vinalopó",   "https://coordinacionaltovinalopo.onrender.com/"),
            (3, "Zona 3 · Bajo Vinalopó",   "https://coordinacionbajovinalopo.onrender.com/"),
            (4, "Zona 4 · Alcoià / Comtat", "https://coordinacionalcoy.onrender.com/"),
            (5, "Zona 5 · Marina Alta",     "https://coordinacionmarinaalta.onrender.com/"),
            (6, "Zona 6 · Marina Baixa",    "https://coordinacionmarinabaixa.onrender.com/"),
            (7, "Zona 7 · Elche y entorno", "https://coordinacionelche.onrender.com/"),
            (8, "Zona 8 · Vega Baja",       "https://coordinacionvegabaja.onrender.com/"),
        ]

        for zid, nombre, url in ZONAS_DEF:
            zona = Zona.query.get(zid)
            if not zona:
                db.session.add(Zona(id=zid, nombre=nombre, url=url))
            else:
                # por si cambias la URL en el futuro
                zona.url = url

        db.session.commit()

        # --- Usuario admin por defecto ---
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


# Instancia global que usa gunicorn
app = create_app()


