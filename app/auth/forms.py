from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    pasword = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=4)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')