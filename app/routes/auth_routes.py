from . import main_bp
from flask import render_template

@main_bp.route('/register')
def register():
    return render_template('register.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')