from flask import render_template
from . import zonas_bp

@zonas_bp.route('/')
def index():
    return render_template('zonas/index.html')
