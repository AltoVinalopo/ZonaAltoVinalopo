import os
from flask import render_template, current_app
from flask_login import login_required
from . import zonas_bp

@zonas_bp.route("/")
@login_required
def index():
    # Leer carpetas dentro de /zonas/
    base = os.path.join(current_app.root_path, "zonas")
    carpetas = []

    for nombre in sorted(os.listdir(base)):
        ruta = os.path.join(base, nombre)
        if os.path.isdir(ruta) and "Zona" in nombre:
            carpetas.append(nombre)

    return render_template("zonas_index.html", carpetas=carpetas)
