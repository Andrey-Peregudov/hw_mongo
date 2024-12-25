import os
import uuid

from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_required
from app.main import app, db
from app.models import Tovar
from .forms import TovarForm

tovar_bp = Blueprint('tovari', __name__, template_folder='templates', static_folder='static')
@tovar_bp.route('/tovar_add', methods=['GET', 'POST'])
@login_required
def tovar_add():
    # flash(current_user.name)
    form = TovarForm()
    print('Func add work')
    if form.validate_on_submit():

        # загрузка файла для дальнейшей обработки
        file = request.files['file']
        print(file.mimetype)

        rasshirenie = file.filename.split(".")[-1]
        print(rasshirenie)
        new_filename = uuid.uuid4().hex
        save_file_name = new_filename + '.' + rasshirenie
        list_ok = ['jpg', 'png']

        if rasshirenie not in list_ok:
            return 'Ne to!'

        # сохранение
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], save_file_name))

        name = form.name.data
        price = form.price.data
        ostatok = form.ostatok.data
        data = Tovar(name=name, price=int(price), ostatok=int(ostatok), url_photo=save_file_name)
        db.session.add(data)
        db.session.commit()
        flash('Товар добавлен')
        return redirect(url_for('home.index'))
    return render_template('tovar_add.html', form=form)


@tovar_bp.route('/tovar_del/<tovar_id>', methods=['GET', 'POST'])
def del_tovar(tovar_id: int):
    data = Tovar.query.get(tovar_id)
    # data = Tovar.query.select(Tovar.id == tovar_id).one()
    # data = Tovar.query.where(Tovar.id == tovar_id).one()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('home.index'))


@tovar_bp.route('/tovar_kupit', methods=['GET', 'POST'])
def tovar_kupit():
    id = request.args.get('id')
    print(id)
    global korzina
    data = Tovar.query.get(id)
    korzina.append(data)
    data.ostatok = data.ostatok - 1
    db.session.commit()
    print(data)
    return redirect(url_for('home.index'))


@tovar_bp.route('/tovar_page', methods=['GET', 'POST'])
def tovar_page():
    id = request.args.get('id')
    print(id)
    data = Tovar.query.get(id)
    print(data)
    return render_template('tovar_page.html', data=data)


@tovar_bp.route('/tovar_new_name/<tovar_id>/<new_name>', methods=['GET', 'POST'])
def name_tovar(tovar_id: int, new_name: str):
    data = Tovar.query.get(tovar_id)
    data.name = new_name
    db.session.commit()
    return redirect(url_for('home.index'))