from flask import Blueprint, render_template

error_bp = Blueprint('error', __name__, template_folder='templates', static_folder='static')


@error_bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@error_bp.errorhandler(400)
def error_400(error):
    return render_template('400.html'), 400


@error_bp.errorhandler(401)
def error_401(error):
    return render_template('401.html'), 401


@error_bp.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
