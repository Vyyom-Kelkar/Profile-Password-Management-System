from app import db
from flask import request
from models import mysession, User, Admin_Setting, Old_Password, Common_Password, engine
from sqlalchemy import update
from datetime import datetime
from similarityAlgorithm import similar
from compareOldToNewPassword import newPasswordToOldPasswordComparison 
from hashPassword import hashPassword
from verify import verifyPassword

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
	if verifyPassword(Password, userPass):
		return True
	else:
		return False

def verifyChange(request):
	userEmail = request.form['email']
	userPass = request.form['oldPassword']
	user = mysession.query(User).filter_by(email=userEmail).first()
	Password = user.current_password
	if verifyPassword(Password, userPass):
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
	userCurrPass = hashPassword(userCurrPass)

  	myUser = User(name=userName, current_password=userCurrPass, is_admin=adminStatus, email=userEmail, company_name=userCompany, phone_number=userPhone, password_last_set=userLastSet, token=None, last_login=userLastLogin)
  	mysession.add(myUser)
	mysession.commit()

def changePassword(request):
	userEmail = request.form['email']
	newPassword = request.form['password']
	newPassword = hashPassword(newPassword)
	mysession.query(User).filter_by(email=userEmail).update({"current_password": newPassword})

def getCompany(request):
	userEmail = request.form['email']
	user = mysession.query(User).filter_by(email=userEmail).first()
	userCompany = user.company_name
	return getCompanyRequirements(userCompany)

def company(request):
	userEmail = request.form['email']
	user = mysession.query(User).filter_by(email=userEmail).first()
	userCompany = user.company_name
	return userCompany

def companyExists(request):
	userCompany = request.form['company']
	company = mysession.query(Admin_Setting).filter_by(company_name=userCompany).all()
	if(len(company)>0):
		return True
	else:
		return False

def checkWithOldPasswordsAndUpdateChange(request):
	email = request.form['email']
	password = request.form['password']
	oldPassword = request.form['oldPassword']
	oldPasswords = mysession.query(Old_Password).filter_by(userEmail = email).all()
	oldPasswordsArr = []
	for i in oldPasswords:
		oldPasswordsArr.append(i.hashed_password)

	responseArray = newPasswordToOldPasswordComparison(password, oldPassword, oldPasswordsArr)
	if(responseArray[0]):
		newHashedPassword = responseArray[1]
		mysession.query(User).filter_by(email = email).update({"current_password": newHashedPassword})
		oldPassword = hashPassword(oldPassword)
		newRow = Old_Password(userEmail = email, hashed_password = oldPassword)
		mysession.add(newRow)
		mysession.commit()
		return True
	else:
	  return False 

def checkWithOldPasswordsAndUpdate(request):
	userEmail = request.form['email']
	password = request.form['password']
	objectOldPasswords = mysession.query(Old_Password).filter_by(userEmail = userEmail).all()
	oldPasswordsArr = []
	for i in objectOldPasswords:
		oldPasswordsArr.append(i.hashed_password)

	responseArray = similar(password, oldPasswordsArr)
	print responseArray	
#if(responseArray[0]):
#	   newHashedPassword = responseArray[1]
#	   mysession.query(User).filter_by(email=userEmail).update({"current_password": newHashedPassword})
#	else:
#	  return False 

def addAdminSettings(form, companyName):
	passLength = form.plength.data
	requireCaps = form.caps.data
	requireLow = form.lowercase.data
	requireNum = form.numeric.data
	requireSpec = form.special.data
	expDays = form.expiration.data
		
	mySettings = Admin_Setting(company_name=companyName, password_length=passLength, require_caps=requireCaps, require_lowercase=requireLow, require_number=requireNum, require_special=requireSpec, expiration_days=expDays)
	mysession.add(mySettings)
	mysession.commit()

def verifyAdmin(request):
	userEmail = request.form['email']
	userPass = request.form['password']
	user = mysession.query(User).filter_by(email=userEmail).first()
	Password = user.current_password
	if verifyPassword(Password, userPass):
		return user.is_admin
	else:
 		return False

def updateAdminSettings(form, companyName):
	passLength = form.plength.data
	requireCaps = form.caps.data
	requireLow = form.lowercase.data
	requireNum = form.numeric.data
	requireSpec = form.special.data
	expDays = form.expiration.data
  
	mysession.query(Admin_Setting).filter_by(company_name=companyName).update({"password_length": passLength})
	mysession.query(Admin_Setting).filter_by(company_name=companyName).update({"require_caps": requireCaps})
	mysession.query(Admin_Setting).filter_by(company_name=companyName).update({"require_lowercase": requireLow})
	mysession.query(Admin_Setting).filter_by(company_name=companyName).update({"require_number": requireNum})
	mysession.query(Admin_Setting).filter_by(company_name=companyName).update({"require_special": requireSpec})
