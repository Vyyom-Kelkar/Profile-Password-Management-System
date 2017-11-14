from app import db
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
