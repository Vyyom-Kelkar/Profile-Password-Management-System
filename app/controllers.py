from app import db
from flask import request
from models import mysession, User, Admin_Setting, Old_Password, Common_Password, engine
from sqlalchemy import update
from datetime import datetime


'''
1) GET : list_object = mysession.query(TABLE_NAME).filter_by(expressions with commas).all()
	use a for loop to iterate through the list and handle attributes

2) PATCH (update) : patch_object = update(TABLE_NAME).where(expressions with commas).values(attribute_name = "value")
		   engine.execute(patch_object)

3) POST : row_object = TABLE_NAME(list of attribute_name = "value")
		  mysession.add(row_object)


---------
EXAMPLES
---------

# GET
list = mysession.query(User).filter_by(company_name="Bad Company", ID=3).all()
for x in range(0, len(list)):
	print (list[x].name + " " + list[x].email)

# PATCH
s = update(User).where(User.ID==1).values(name="brett")
engine.execute(s)

# POST
row = Common_Password(ID=112, hashed_password="yydhdhdhd")
mysession.add(row)

'''

def testfunction(myemail):
	login = datetime(1996, 1, 2, 3, 4, 5)
	print login
	myuser = User(ID=10,name='Brett',current_password='doggy',is_admin=1,email=myemail,company_name='Google',phone_number='614-234-5464',password_last_set=login, token='akjv;asv;av;alkv',last_login=login)
	mysession.add(myuser)
	mysession.commit()
	data = mysession.query(User).filter_by(ID=9).all()
	print data[0].ID
	print data[0].email

def verify(request):
	userEmail = request.form['email']
	userPass = request.form['password']
	print userEmail
	print userPass
	user = mysession.query(User).filter_by(email=userEmail).first()
	Password = user.current_password
	if userPass == Password:
		return True
	else:
		return False

def uniqueEmail(request):
	userEmail = request.form['email']
	user = mysession.query(User).filter_by(email=userEmail).all()
	if len(user) > 0:
		return False
	else:
		return True

def getCompanyRequirements(company):
	settings = mysession.query(Admin_Setting).filter_by(company_name=company).first()
	settingsArray = [settings.password_length,settings.require_caps,settings.require_lowercase,settings.require_number,settings.require_special,settings.expiration_days]
	return settingsArray 

def addUser(user, password):
	today = datetime(1996, 1, 2, 3, 4, 5)
	userName = user[0]
	userCurrPass = password 
	adminStatus = (user[4] == 'admin')
	userEmail = user[1]
	userCompany = user[2]
	userPhone = user[3]
	userLastSet = today
	userLastLogin = today

  	myUser = User(name=userName, current_password=userCurrPass, is_admin=adminStatus, email=userEmail, company_name=userCompany, phone_number=userPhone, password_last_set=userLastSet, token=None, last_login=userLastLogin)
  	mysession.add(myUser)
	mysession.commit()

def changePassword(request):
	userEmail = request.form['email']
	newPassword = request.form['password']
	mysession.query(User).filter_by(email=userEmail).update({"current_password": newPassword})

def getCompany(request):
	userEmail = request.form['email']
	user = mysession.query(User).filter_by(email=userEmail).first()
	userCompany = user.company_name
	return getCompanyRequirements(userCompany)
