from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random as rand

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

@app.route("/randomnum")
for number in range(0,4):
    account_number = ""
    random_number = str(rand.randint(0,9))
    account_number += random_number
    new_acc = print(account_number,end="")

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)

