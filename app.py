# app.py

from flask import Flask
from flask_login import LoginManager
from modelos.usuario import Usuario
from auth import auth_bp
from zonas import zonas_bp
from ayuntamientos import aytos_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = "MI_CLAVE_SUPER_SECRETA_123456"

    # LOGIN
    login = LoginManager()
    login.login_view = "auth.login"
    login.init_app(app)

    @login.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # BLUEPRINTS
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(zonas_bp)
    app.register_blueprint(aytos_bp, url_prefix="/ayuntamientos")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


