from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, URL



class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("	Password", validators=[DataRequired()])
    submit = SubmitField("Login")
