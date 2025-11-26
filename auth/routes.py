from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from . import auth_bp
from modelos.user import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if current_user.is_authenticated:
        return redirect(url_for('aytos_bp.panel'))

    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            error = "Usuario o contraseña incorrectos"
        else:
            login_user(user)
            return redirect(url_for('aytos_bp.panel'))

    return render_template('login.html', error=error)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


