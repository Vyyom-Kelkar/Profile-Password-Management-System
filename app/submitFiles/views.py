# This file creates the routes for the views
# Dakota Duncan


from flask import url_for, render_template, session, request, flash, redirect
from app import app
from .forms import AdminForm, LoginForm, SignupForm, NewForm, ForgotForm, ChangeForm, ForgotChangeForm
from controllers import updateAdminSettings, verifyAdmin, company, checkWithOldPasswordsAndUpdateChange, addAdminSettings, addAdminSettings, companyExists, checkWithOldPasswordsAndUpdate, verifyChange, changePassword, getCompany, addUser, verify, mysession, uniqueEmail, getCompanyRequirements
from checkPasswordWithCompanySettings import checkPasswordWithCompanySettings 
from models import User, Admin_Setting

# Route for home page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title = 'Home')

# Route for sign in page
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and verify(request):
		return redirect('/decisions')
	return render_template('login.html', title = 'Sign In', form = form)

# Route for sign up page
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'POST' and uniqueEmail(request):
		session['name'] = request.form['name']
		session['email'] = request.form['email']
		session['company'] = request.form['company']
		session['phone'] = request.form['phone']
		session['userType'] = request.form['userType']
		if request.form['userType'] == 'admin' and not companyExists(request):
			return redirect('/newAdmin')		
		return redirect('/newCredentials')
	return render_template('signup.html', title = 'Sign Up', form = form)

# Route for page to create new credentials
@app.route('/newCredentials', methods=['GET', 'POST'])
def newCredentials():
	form = NewForm()
	requirements = getCompanyRequirements(session['company'])
	user = [session['name'], session['email'], session['company'], session['phone'], session['userType']]
	if request.method == 'POST' and checkPasswordWithCompanySettings(requirements, request.form['password']):
		addUser(user, request.form['password'])
		return redirect('/decisions')
	return render_template('newCredentials.html', title = 'New', form = form)

# Route for forgotten password page
@app.route('/forgot')
def forgot():
	form = ForgotForm()
	return render_template('forgot.html', title = 'Forgotten Password', form = form)

# Route for main page
@app.route('/decisions')
def decisions():
	return render_template('decisions.html', title = 'Main')

# Route for change password page
@app.route('/change', methods=['GET', 'POST'])
def change():
	form = ChangeForm()
	if request.method == 'POST' and verifyChange(request):
		requirements = getCompany(request)
		if checkPasswordWithCompanySettings(requirements, request.form['password']) and checkWithOldPasswordsAndUpdateChange(request):
			return redirect('/decisions')
	return render_template('change.html', title = 'Change', form = form)

# Route for verify admin page
@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
	form = LoginForm()
	if request.method == 'POST' and verifyAdmin(request):
		session['company'] = company(request)
		return redirect ('/admin')
	return render_template('confirm.html', title = 'Admin', form = form)

# Route for admin page
@app.route('/admin', methods = ['POST', 'GET'])
def admin():
	form = AdminForm()
	if request.method == 'POST':
		updateAdminSettings(form, session['company'])
		return redirect('/decisions')
	return render_template('admin.html', title = 'Admin', form = form)

# Route for new admin settings page
@app.route('/newAdmin', methods = ['GET', 'POST'])
def newAdmin():
	form = AdminForm()
	if request.method == 'POST':
		addAdminSettings(form, session['company'])
		return redirect('/newCredentials')
	return render_template('newAdmin.html', title = 'newAdmin', form = form)

# Route for forgotten password change page
@app.route('/forgotChange', methods = ['GET', 'POST'])
def forgotChange():
	form = ForgotChangeForm()
	if request.method == 'POST':
		checkWithOldPasswordsAndUpdate(request)
		return redirect('/decisions')
	return render_template('forgotChange.html', title = 'Forgot Change', form = form)

# Route for forgotten password confirmation page
@app.route('/forgotConfirmation', methods = ['POST'])
def forgotConfirmation():
	return render_template('forgotConfirmation.html', title = 'Forgot Confirmation')
