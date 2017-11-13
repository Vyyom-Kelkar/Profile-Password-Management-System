from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restless

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
