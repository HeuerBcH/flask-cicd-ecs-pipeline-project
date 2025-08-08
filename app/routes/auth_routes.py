from . import main_bp

@main_bp.route('/register')
def register():
    return "Register Page"