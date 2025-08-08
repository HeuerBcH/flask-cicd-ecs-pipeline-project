from . import main_bp

@main_bp.route('/')
def homepahe():
    return "Hello, CI/CD with Flask!"