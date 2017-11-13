from app import db
from models import mysession, User, Admin_Setting, Old_Password, Common_Password, engine
from sqlalchemy import update

# GET
print (mysession.query(User).filter_by(ID=1).first().name)

# PATCH
s = update(User).where(User.ID==1).values(name="brett")
engine.execute(s)

print (mysession.query(User).filter_by(ID=1).first().name)

# POST
row = Common_Password(ID=112, hashed_password="yydhdhdhd")
mysession.add(row)

print (mysession.query(Common_Password).filter_by(ID=112).first().hashed_password)
