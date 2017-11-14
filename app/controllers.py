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
	myuser = User(ID=9,name='Brett',current_password='doggy',is_admin=1,email=myemail,company_name='Google',phone_number='614-234-5464',password_last_set=login, token='akjv;asv;av;alkv',last_login=login)
	mysession.add(myuser)
	mysession.commit()
	data = mysession.query(User).filter_by(ID=9).all()
	print data[0].ID
	print data[0].email

def verify(request):
  userEmail = request.format(email)
  UserPass = request.format(password)
  pass = mysession.query(User).filter_by(email=userEmail).first()
  if(pass == UserPass)
    return True
  else
    return False

def uniqueEmail(request):
	userEmail = request.form[email]
	emails = mysession.query(User).all()
	if userEmail in emails
		return False
	else
		return True

def companyExists(request):
	userCompany = request.form[company]
	company = mysession.query(Admin_Setting).filter_by(company_name=userCompany)
	if(len(company)>0)
		return True
	else
		return False

def getCompanyRequirements(request):
	userCompany = request.form[company]
	companySettings = mysession.query(Admin_Setting).filter_by(company_name=userCompany).first()
	
	settingsArray = [settings.password_length,settings.require_caps,settings.require_lowercase,settings.require_number,settings.require_special,settings.expiration_days]
	return settingsArray

def addCompany(request):
	compName = request.form[company_name]
	passLength = request.form[password_length]
	requireCaps = request.form[require_caps]
	requireLower = request.form[require_lowercase]
	requireNum = request.form[require_number]
	requireSpec = request.form[require_special]
	expDays = request.form[expiration_days]
  
	myCompany = Admin_Setting(company_name=compName, password_length=passLength, require_caps=requireCaps, require_lowercase=requireLower, require_number, requireNum, require_special=requireSpec, expiration_days=expDays)
  	
	mysession.add(myCompany)
	mysession.commit()
  
def addUser(request):
  	userId = request.form[ID]
	userName = request.form[name]
	userCurrPass = request.form[current_password]
	adminStatus = request.form[is_admin]
	userEmail = request.form[email]
	userCompany = request.form[company_name]
	userPhone = request.form[phone_number]
	userLastSet = request.form[password_last_set]
	userToken = request.form[token]
	userLastLogin = request.form[last_login]

  	myUser = User(ID=userId, name=userName, current_password=userCurrPass, is_admin=adminStatus, email=userEmail, company_name=userCompany, phone_number=userPhone, password_last_set=userLastSet, token=userToken, last_login=userLastLogin)
  	mysession.add(myUser)
	mysession.commit()
  
