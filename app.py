
from flask import Flask, render_template

app = Flask(__name__)

class Municipio:
    def __init__(self, nombre, history="", inhabitants=0, affiliates=0,
                 events=None, info_tables=None, coordinador="", LISTA=None,
                 votos_necesarios=0, team_members=None):
        self.nombre = nombre
        self.history = history
        self.inhabitants = inhabitants
        self.affiliates = affiliates
        self.events = events or []
        self.info_tables = info_tables or {}
        self.coordinador = coordinador
        self.LISTA = LISTA or []
        self.votos_necesarios = votos_necesarios
        self.team_members = team_members or []

municipios = [
    Municipio("Benejama"),
    Municipio("Biar"),
    Municipio("Campo de Mirra"),
    Municipio("Cañada"),
    Municipio("Castalla"),
    Municipio("Onil"),
    Municipio("Sax"),
    Municipio("Villena")
]

@app.route("/")
def index():
    return render_template("index.html", municipios=municipios)

@app.route("/municipio/<nombre>")
def municipio(nombre):
    m = next((x for x in municipios if x.nombre == nombre), None)
    return render_template("municipio.html", municipio=m)

if __name__ == "__main__":
    app.run()
