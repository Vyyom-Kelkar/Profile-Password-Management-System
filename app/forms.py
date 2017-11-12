from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, RadioField
from wtforms.validators import DataRequired

class LoginForm(Form):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])

class SignupForm(Form):
	name = StringField('Name', validators = [DataRequired()])
	email = StringField('Email', validators = [DataRequired()])
	company = StringField('Company', validators = [DataRequired()])
	address = StringField('Address', validators = [DataRequired()])
	phone = IntegerField('Phone', validators = [DataRequired()])
	userType = RadioField('User Type', choices = [('value', 'Admin'), ('value_two', 'Employee')])

class NewForm(Form):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired()])

class ForgotForm(Form):
	email = StringField('Email', validators = [DataRequired()])
