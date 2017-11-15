from app import db
from flask import request
from models import mysession, User, Admin_Setting, Old_Password, Common_Password, engine
from sqlalchemy import update
from datetime import datetime
from similarityAlgorithm import similar
from compareOldToNewPassword import newPasswordToOldPasswordComparison 
from hashPassword import hashPassword

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

def verify(request):
	userEmail = request.form['email']
	userPass = request.form['password']
	user = mysession.query(User).filter_by(email=userEmail).first()
	Password = user.current_password
	if userPass == Password:
		return True
	else:
		return False

def verifyChange(request):
	userEmail = request.form['email']
	userPass = request.form['oldPassword']
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

def companyExists(request):
	userCompany = request.form['company']
	company = mysession.query(Admin_Setting).filter_by(company_name=userCompany).all()
	if(len(company)>0):
		return True
	else:
		return False

def checkWithOldPasswordsAndUpdate(email):
#userEmail = request.form['email']
#password = request.form['password']
	password = 'sportsball1'	
	oldPassword = 'sportsball'
	objectOldPasswords = mysession.query(Old_Password).filter_by(userEmail = email).all()
	oldPasswords = []
	for i in objectOldPasswords:
		oldPassword = hashPassword(i.hashed_password)	
		oldPasswords.append(oldPassword)

	responseArray = newPasswordToOldPasswordComparison(password, oldPassword, oldPasswords)
	print responseArray	
#if(responseArray[0]):
#	   newHashedPassword = responseArray[1]
#	   mysession.query(User).filter_by(email=userEmail).update({"current_password": newHashedPassword})
#	else:
#	  return False 

def addAdminSettings(request, companyName):
	passLength = request.form['plength']
	requireCaps = request.form['caps']
	requireLow = request.form['lowercase']
	requireNum = request.form['numeric']
	requireSpec = request.form['special']
	expDays = request.form['expiration']
  	
 	mySettings = Admin_Settings(company_name=companyName, password_length=passLength, require_caps=requireCaps, require_lowercase=requireLow, require_number=requireNum, require_special=requireSpec, expiration_days=expDays)
  mysession.add(mySettings)
	mysession.commit()
