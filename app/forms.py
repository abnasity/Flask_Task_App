from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
     title = StringField('Task Title', validators=[DataRequired()])
     description = TextAreaField('Task Description', validators=[DataRequired()])
     completed = BooleanField('Completed')
     submit = SubmitField('Submit', validators=[DataRequired()])
     
class UserForm(FlaskForm):
     
     username = StringField('User', validators=[DataRequired()])
     first_name = StringField('First Name',  validators=[DataRequired()])
     last_name = StringField('Last Name',  validators=[DataRequired()])
     password = PasswordField('Password',  validators=[DataRequired()])
 
     submit = SubmitField('Register')
     
class LoginForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired()])
     password = PasswordField('password', validators=[DataRequired()])
     submit = SubmitField('Login')