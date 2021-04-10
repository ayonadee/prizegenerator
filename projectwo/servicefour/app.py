from flask import Flask, render_template, request, url_for, jsonify
import requests
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# db = SQLAlchemy(app)

@app.route("/prizegenerator", methods=['GET','POST'])
def prizegenerator():
    account_number = ""
    cashprize = 10000
    prize = 0
    randomletter = requests.get("http://servicethree:5002/randomletter").text
    randomnum = requests.get("http://servicetwo:5001/randomnum").text
    account_number = randomnum + randomletter
    if randomletter[0] == 'a' or '4' in randomnum:
        prize = 50/100 * cashprize
        message = f'Congratulations you won £ {prize} which is 50 per cent of the crash prize!'
    else:
        message = 'Sorry but your account number does not qualify for the cash prize,better luck next time'
    package = { 'Account_Number': account_number, 'Prize': prize, 'Message': message
    }
    return jsonify(package)


if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)
