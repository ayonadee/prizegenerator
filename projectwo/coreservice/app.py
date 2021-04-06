from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import random as rand
import string


app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email, ' Name: ', self.first_name, ' ', self.last_name, '\n'])


@app.route('/')
def homepage():
		return render_template('home.html')
    
	
@app.route('/home', methods=['POST','GET'])
def home():
	home = requests.get("http://servicefour:5003/prizegenerator")
    

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/test', methods=['POST', 'GET'])
# def test():
#     test = requests.get('http://logic_s4:5004/logic')
#     print("hello")
#     print(test.text)
#     test = test.text
#     return render_template('test.html', test = test)
	# data1 = Users.query.all()
    # return render_template('home.html', data1=data1)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)