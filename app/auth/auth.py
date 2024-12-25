from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user

from .forms import LoginForm
from ..main import db
from ..models import User


from pymongo import MongoClient
import json
from bson import ObjectId

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth_bp.route('/user_data', methods=['GET', 'POST'])
def user_data():
    if current_user.is_authenticated:
        return render_template('user_data.html', user=current_user)
    else:
        return redirect(url_for('error.not_found_error'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        print('*' * 20)
        print(user)
        if user is None or not user.check_password(form.pasword.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('home.index'))
    return render_template('login_enter.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('mongo', 27017)
db = client['flask_mongodb']
collection = db['users']



@auth_bp.route('/user_reg', methods=['GET', 'POST'])
def user_reg():
    form3 = LoginForm()
    if form3.validate_on_submit():
        name = form3.username.data
        data = User(name=form3.username.data, is_active=False)
        data.set_password(form3.pasword.data)
        db.session.add(data)
        db.session.commit()

        mongo_data = {'name': name, 'password': form.password.data}
        collection.insert_one(mongo_data)
        flash(f'ПОЛЬЗОВАТЕЛЬ {name} ЗАРЕГИСТРИРОВАН')
        return redirect(url_for('home.index'))
    return render_template('user_reg.html', form2=form3)
