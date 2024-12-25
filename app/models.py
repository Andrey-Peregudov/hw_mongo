import sqlalchemy as sa
from flask_admin.contrib.sqla import ModelView

from sqlalchemy.orm import relationship
from .main import db, login_manager, admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    password_hash = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    phone_number = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    is_active = sa.Column(sa.Boolean, default=True)
    admin = sa.Column(sa.Boolean, default=False)

    address = db.relationship('Address', backref='address', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


admin.add_view(SecureModelView(User, db.session))


class Address(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    city = sa.Column(sa.String(255))
    ulica = sa.Column(sa.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


admin.add_view(SecureModelView(Address, db.session))


class Categories(db.Model):
    __tablename__ = 'categories'
    id = sa.Column(sa.Integer, primary_key=True)
    product_type = sa.Column(sa.String(255))
    appointment = sa.Column(sa.String(255))
    brand = sa.Column(sa.String(255))

    tovars = db.relationship('Tovar', back_populates='category', lazy='dynamic')


admin.add_view(SecureModelView(Categories, db.session))


class Tovar(db.Model):
    __tablename__ = 'tovars'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    url_photo = sa.Column(sa.String(255), nullable=True)
    price = sa.Column(sa.Integer, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    ostatok = sa.Column(sa.Integer, default=0)

    category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
    category = relationship('Categories', back_populates='tovars')


admin.add_view(SecureModelView(Tovar, db.session))
