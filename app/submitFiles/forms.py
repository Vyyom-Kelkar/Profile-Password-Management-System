from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, IntegerField, RadioField
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
	userType = RadioField('User Type', choices = [('admin', 'Admin'), ('employee', 'Employee')])

class NewForm(Form):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired()])

class ForgotForm(Form):
	email = StringField('Email', validators = [DataRequired()])

class ChangeForm(Form):
	email = StringField('Email', validators = [DataRequired()])
	oldPassword = PasswordField('Old Password', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired()])

class AdminForm(Form):
	plength = IntegerField('Password Length', validators = [DataRequired()])
	caps = BooleanField('Password must contain capital letters', validators = [DataRequired()])
	lowercase = BooleanField('Password must contain lowercase letters', validators = [DataRequired()])
	numeric = BooleanField('Password must contain numeric characters', validators = [DataRequired()], false_values={'false',''})
	special = BooleanField('Password must contain special characters (!@#$%*&)', validators = [DataRequired()])
	expiration = IntegerField('Expiration', validators = [DataRequired()])

class ForgotChangeForm(Form):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirmPassword = PasswordField('Confirm Password', validators = [DataRequired()])
