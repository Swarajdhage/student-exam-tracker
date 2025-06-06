from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, Length

from wtforms import BooleanField

from flask_wtf.file import FileField, FileAllowed

class ExamForm(FlaskForm):
    name = StringField('Exam Name', validators=[InputRequired()])
    date = DateField('Exam Date', format='%Y-%m-%d', validators=[InputRequired()])
    application_file = FileField('Upload Application File', validators=[FileAllowed(['pdf', 'png', 'jpg'])])
    fee_file = FileField('Upload Fee Receipt', validators=[FileAllowed(['pdf', 'png', 'jpg'])])
    submit = SubmitField('Save')



class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    phone = StringField('Phone Number')
    gender = SelectField('Gender', choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = DateField('Date of Birth', format='%Y-%m-%d')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
