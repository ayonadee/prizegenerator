from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

@app.route("\prizegenerator")
random = requests.get("http://servicethree:5002/random")
random = requests.get("http://servicetwo:5001/random")
servicetwo = requests.get('http://localhost:5001')
servicethree = requests.get('http://localhost:5002')
    
cashprize = 10000
your_account_number = new_acc.append(newlett)
if your_account_number[0] == 1:
    prize = 25/100 * cashprize
    print('congratulations you won', prize, 'which is 50 per cent of the crash prize')
else:
    print('Sorry but your account number does bot qualify for the cash prize')

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)
