# zonas/routes.py
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

zonas_bp = Blueprint("zonas", __name__)

# ============================
#  DEFINICIÓN COMPLETA DE ZONAS
# ============================

ZONAS = [
    {
        "id": 1,
        "slug": "zona1-alacanti",
        "nombre": "Zona 1 · Alacantí",
        "descripcion": "Municipios del área de l'Alacantí.",
        "url": "https://coordinacionalacanti.onrender.com/",
    },
    {
        "id": 2,
        "slug": "zona2-altovinalopo",
        "nombre": "Zona 2 · Alto Vinalopó",
        "descripcion": "Coordinación de la zona Alto Vinalopó.",
        "url": "https://coordinacionaltovinalopo.onrender.com/",
    },
    {
        "id": 3,
        "slug": "zona3-bajovinalopo",
        "nombre": "Zona 3 · Bajo Vinalopó",
        "descripcion": "Coordinación de la zona Bajo Vinalopó.",
        "url": "https://coordinacionbajovinalopo.onrender.com/",
    },
    {
        "id": 4,
        "slug": "zona4-alcoy",
        "nombre": "Zona 4 · Alcoià / Comtat",
        "descripcion": "Coordinación de la zona Alcoià / Comtat.",
        "url": "https://coordinacionalcoy.onrender.com/",
    },
    {
        "id": 5,
        "slug": "zona5-marinaalta",
        "nombre": "Zona 5 · Marina Alta",
        "descripcion": "Coordinación de la zona Marina Alta.",
        "url": "https://coordinacionmarinaalta.onrender.com/",
    },
    {
        "id": 6,
        "slug": "zona6-marinabaja",
        "nombre": "Zona 6 · Marina Baixa",
        "descripcion": "Coordinación de la zona Marina Baixa.",
        "url": "https://coordinacionmarinabaixa.onrender.com/",
    },
    {
        "id": 7,
        "slug": "zona7-elche",
        "nombre": "Zona 7 · Elche y entorno",
        "descripcion": "Coordinación de la zona de Elche.",
        "url": "https://coordinacionelche.onrender.com/",
    },
    {
        "id": 8,
        "slug": "zona8-vegabaja",
        "nombre": "Zona 8 · Vega Baja",
        "descripcion": "Coordinación de la Vega Baja.",
        "url": "https://coordinacionvegabaja.onrender.com/",
    },
]

# ============================
#  LISTADO GENERAL DE ZONAS
# ============================

@zonas_bp.route("/")
@login_required
def zonas_index():
    return render_template(
        "zonas_index.html",
        usuario=current_user,
        zonas=ZONAS,
    )

# ============================
#  DETALLE DE UNA ZONA (CARGA LA WEB REAL CON IFRAMED)
# ============================

@zonas_bp.route("/<slug>/")
@login_required
def zona_detalle(slug):
    zona = next((z for z in ZONAS if z["slug"] == slug), None)
    if not zona:
        abort(404)

    return render_template(
        "zona_detalle.html",
        usuario=current_user,
        zona=zona,
    )
