from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

@app.route("/randomletter")
for letter in range(0,4):
    random_letter = ''
    lower_alphabet = string.ascii_letters.lower()
    random_generated_letter = rand.choice(lower_alphabet)
    random_letter += random_generated_letter
    newletter = print(random_letter, end="")



if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)
