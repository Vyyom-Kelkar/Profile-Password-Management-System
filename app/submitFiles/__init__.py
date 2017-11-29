# This file initializes the flask application
# Vyyom Kelkar

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of a Flask application
app = Flask(__name__)

# Configure the application from config.py file
app.config.from_object('config')

# Create an instance of SQLAlchemy for the Flask application
db = SQLAlchemy(app)

from app import views, models, controllers

