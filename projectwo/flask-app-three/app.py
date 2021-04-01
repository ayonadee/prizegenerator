from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'



