from flask import url_for, render_template, session, request, flash, redirect
from app import app
from .forms import AdminForm, LoginForm, SignupForm, NewForm, ForgotForm, ChangeForm, ForgotChangeForm
from similarityAlgorithm import similar
from controllers import verify, testfunction 

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Home')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and verify(request):
		return redirect('/decisions')
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST':
		session['company'] = request.form['company']
		return redirect('/newCredentials')
	return render_template('signup.html', title = 'Sign Up', form = form)

@app.route('/newCredentials', methods=['GET', 'POST'])
def newCredentials():
	form = NewForm()
	print session['company']
	return render_template('newCredentials.html', title = 'New', form = form)

@app.route('/forgot')
def forgot():
	form = ForgotForm()
	return render_template('forgot.html', title = 'Forgotten Password', form = form)

@app.route('/decisions')
def decisions():
	return render_template('decisions.html', title = 'Main')

@app.route('/change')
def change():
	form = ChangeForm()
	return render_template('change.html', title = 'Change', form = form)

@app.route('/confirm')
def confirm():
	form = LoginForm()
	return render_template('confirm.html', title = 'Admin', form = form)

@app.route('/admin')
def admin():
	form = AdminForm()
	return render_template('admin.html', title = 'Admin', form = form)

@app.route('/forgotChange')
def forgotChange():
	form = ForgotChangeForm()
	return render_template('forgotChange.html', title = 'Forgot Change', form = form)

@app.route('/forgotConfirmation', methods = ['POST'])
def forgotConfirmation():
	email = request.form['email']
	testfunction(email)
	return render_template('forgotConfirmation.html', title = 'Forgot Confirmation')
