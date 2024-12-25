from flask import Blueprint, render_template

blueprint_bp_dz = Blueprint('bp_dz_', __name__, template_folder='templates', static_folder='static')

@blueprint_bp_dz.route('/bp_dz/')
def bp_dz():
    return render_template('bp_dz.html', new_blueprint='Blueprint DZ')