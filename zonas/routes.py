# zonas/routes.py
from flask import render_template, abort
from flask_login import login_required, current_user

from . import zonas_bp

# Definición de las 8 zonas (puedes ajustar nombres/texto)
ZONAS = [
    {
        "slug": "zona1-alacanti",
        "nombre": "Zona 1 · Alacantí",
        "descripcion": "Municipios del área de l'Alacantí.",
    },
    {
        "slug": "zona2-altovinalopo",
        "nombre": "Zona 2 · Alto Vinalopó",
        "descripcion": "Coordinación de la zona Alto Vinalopó.",
    },
    {
        "slug": "zona3-bajovinalopo",
        "nombre": "Zona 3 · Bajo Vinalopó",
        "descripcion": "Coordinación de la zona Bajo Vinalopó.",
    },
    {
        "slug": "zona4-alcoy",
        "nombre": "Zona 4 · Alcoià / Comtat",
        "descripcion": "Coordinación de la zona Alcoià / Comtat.",
    },
    {
        "slug": "zona5-marinaalta",
        "nombre": "Zona 5 · Marina Alta",
        "descripcion": "Coordinación de la zona Marina Alta.",
    },
    {
        "slug": "zona6-marinabaja",
        "nombre": "Zona 6 · Marina Baixa",
        "descripcion": "Coordinación de la zona Marina Baixa.",
    },
    {
        "slug": "zona7-elche",
        "nombre": "Zona 7 · Elche y entorno",
        "descripcion": "Coordinación de la zona de Elche.",
    },
    {
        "slug": "zona8-vegabaja",
        "nombre": "Zona 8 · Vega Baja",
        "descripcion": "Coordinación de la Vega Baja.",
    },
]


@zonas_bp.route("/")
@login_required
def index():
    """
    Listado de zonas para el panel principal.
    """
    return render_template(
        "zonas_index.html",
        usuario=current_user,
        zonas=ZONAS,
    )


@zonas_bp.route("/<slug>/")
@login_required
def detalle_zona(slug):
    """
    Detalle de una zona concreta.
    De momento sólo muestra una página sencilla de esa zona.
    Más adelante aquí podemos incrustar el proyecto de cada carpeta
    (Zona1Alacanti, Zona2AltoVinalopo, etc.).
    """
    zona = next((z for z in ZONAS if z["slug"] == slug), None)
    if not zona:
        abort(404)

    return render_template(
        "zona_detalle.html",
        usuario=current_user,
        zona=zona,
    )
