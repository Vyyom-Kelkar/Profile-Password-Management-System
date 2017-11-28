# Configuration settings for the flask application
# Vyyom Kelkar

# Enable forms and entries
WTF_CSRF_ENABLED = True

SECRET_KEY = 'youwillneverguess'

# Declare the database for the application, the folder for the migrations and settings for tracking modifications
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/app.db'
SQLALCHEMY_MIGRATE_REPO = 'db_repository'
SQLALCHEMY_TRACK_MODIFICATIONS = False
