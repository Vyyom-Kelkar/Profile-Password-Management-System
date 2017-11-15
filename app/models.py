from app import db
from app import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_restless import APIManager

Base = declarative_base()

class Admin_Setting(Base):
	__tablename__ = 'Admin_Setting'

	company_name = db.Column(db.String(50), primary_key=True)
	password_length = db.Column(db.Integer, nullable=False)
	require_caps = db.Column(db.Boolean, nullable=False)
	require_lowercase = db.Column(db.Boolean, nullable=False)
	require_number = db.Column(db.Boolean, nullable=False)
	require_special = db.Column(db.Boolean, nullable=False)
	expiration_days = db.Column(db.Integer, nullable=False)

class User(Base):
	__tablename__ = 'User'
	
	email = db.Column(db.String(50), primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	current_password = db.Column(db.String(50), nullable=False)
	is_admin = db.Column(db.Boolean, nullable=False)
	company_name = db.Column(db.String(50), db.ForeignKey('Admin_Setting.company_name'), nullable=False)
	phone_number = db.Column(db.String(12), nullable=False)
	password_last_set = db.Column(db.DateTime, nullable=False)
	token = db.Column(db.String(30), nullable=True)
	last_login = db.Column(db.DateTime, nullable=False)
	Admin_Setting = db.relationship(Admin_Setting)

class Old_Password(Base):
	__tablename__ = 'Old_Password'

	userEmail = db.Column(db.Integer, db.ForeignKey('User.email'), primary_key=True)
	hashed_password = db.Column(db.String(50), nullable=False, primary_key=True)
	User = db.relationship(User)

class Common_Password(Base):
	__tablename__ = 'Common_Password'

	hashed_password = db.Column(db.String(50), primary_key=True)

engine = create_engine('sqlite:///db/app.db')
Base.metadata.create_all(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = Session() 


manager = APIManager(app, session=mysession)
manager.create_api(User, methods=['GET', 'POST', 'PATCH'])
manager.create_api(Admin_Setting, methods=['GET', 'POST', 'PATCH'])
manager.create_api(Old_Password, methods=['GET', 'POST', 'PATCH'])
manager.create_api(Common_Password, methods=['GET', 'POST', 'PATCH'])
