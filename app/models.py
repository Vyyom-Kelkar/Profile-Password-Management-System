from app import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Admin_Setting(Base):
	__tablename__ = 'Admin_Setting'

	company_name = db.Column(db.String(50), nullable=False, primary_key=True)
	password_length = db.Column(db.Integer, nullable=False)
	require_caps = db.Column(db.Boolean, nullable=False)
	require_lowercase = db.Column(db.Boolean, nullable=False)
	require_number = db.Column(db.Boolean, nullable=False)
	require_special = db.Column(db.Boolean, nullable=False)
	expiration_days = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return '<Admin_Setting %r>' %(self.nickname)

class User(Base):
	__tablename__ = 'User'

	ID = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	current_password = db.Column(db.String(50), nullable=False)
	is_admin = db.Column(db.Boolean, nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	company_name = db.Column(db.String(50), db.ForeignKey('Admin_Setting.company_name'), nullable=False)
	phone_number = db.Column(db.String(12), nullable=False)
	password_last_set = db.Column(db.DateTime, nullable=False)
	Admin_Setting = db.relationship(Admin_Setting)

	def __repr__(self):
		return '<User %r>' %(self.nickname)

class Old_Password(Base):
	__tablename__ = 'Old_Password'

	ID = db.Column(db.Integer, primary_key=True)
	userID = db.Column(db.Integer, db.ForeignKey('User.ID'), nullable=False)
	hashed_password = db.Column(db.String(50), nullable=False)
	User = db.relationship(User)

	def __repr__(self):
		return '<Old_Password %r>' %(self.nickname)

class Common_Password(Base):
	__tablename__ = 'Common_Password'

	ID = db.Column(db.Integer, primary_key=True)
	hashed_password = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return '<Common_Password %r>' %(self.nickname)

engine = create_engine('sqlite:///db/app.db')
Base.metadata.create_all(engine)