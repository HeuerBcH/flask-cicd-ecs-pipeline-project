from . import main_bp
from flask import redirect, url_for, render_template

@main_bp.route('/')
def index():
    return redirect(url_for('main.login'))

@main_bp.route('/homepage')
def homepage():
    return render_template("homepage.html")