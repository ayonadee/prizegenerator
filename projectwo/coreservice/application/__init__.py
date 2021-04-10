from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import secrets

secret = secrets.token_urlsafe(32)

app.secret_key = secret

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)