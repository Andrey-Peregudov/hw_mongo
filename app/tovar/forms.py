from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import SubmitField, StringField


class TovarForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    price = StringField('Price', validators=[DataRequired(), Length(min=1, max=6)])
    ostatok = StringField('Ostatok')
    submit = SubmitField('Add tovar')

