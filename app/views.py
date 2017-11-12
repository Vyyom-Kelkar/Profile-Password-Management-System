from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, SignupForm, NewForm, ForgotForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/signup')
def signup():
	form = SignupForm()
	return render_template('signup.html', title = 'Sign Up', form = form)

@app.route('/newCredentials')
def newCredentials():
	form = NewForm()
	return render_template('newCredentials.html', title = 'New', form = form)

@app.route('/forgot')
def forgot():
	form = ForgotForm()
	return render_template('forgot.html', title = 'Forgotten Password', form = form)
