from flask import Blueprint

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def homepage():
    return "Hello, CI/CD with Flask!"

@views_bp.route('/register')
def register():
    return "Register Page"