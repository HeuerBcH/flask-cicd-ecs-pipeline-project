from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import home_routes, auth_routes