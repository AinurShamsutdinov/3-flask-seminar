from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    birth_date = DateField('Birth date:', validators=[DataRequired()], format='%d-%m-%Y')
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm password:', validators=[DataRequired(), EqualTo('password')])


class ConfirmAgreement(FlaskForm):
    agreement = BooleanField('Agreement:', validators=[DataRequired('Agreement required')])
