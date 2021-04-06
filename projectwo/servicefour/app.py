from flask import Flask, render_template
import requests
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

@app.route("/prizegenerator")
def prizegenerator():
    account_number = ""
    cashprize = 10000
    randomletter = requests.get("http://servicethree:5002/randomletter").text
    randomnum = requests.get("http://servicetwo:5001/randomnum").text
    account_number = randomnum + randomletter
    for i in range (len(account_number)):
        if account_number[5] == 'a' and '4' in account_number:
            prize = 50/100 * cashprize
            print('Congratulations you won', prize, 'which is 50 per cent of the crash prize!')
        else:
            print('Sorry but your account number does not qualify for the cash prize,better luck next time')
    return f'{str(prize)}'
    # combindedString = ""
    # total_prize = 100
    # user_prize = 0
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # randomString = requests.get('http://random_letters_s2:5002/getRandomString').text
    # randomNumber = requests.get('http://random_numbers_s3:5003/getRandomNumber').text
    # combindedString = randomString + randomNumber
    # for i in range(len(combindedString)):
    #     if(combindedString[i] in vowels):
    #         user_prize += total_prize/10
    #     if(i == 3):
    #         if(combindedString[i] == combindedString[i+1]):
    #             user_prize += (total_prize/10)*2
    #     if(i >= 5):
    #         list_num_val = combindedString[i]
    #         list_num_val = int(list_num_val)
    #         if((list_num_val % 2) == 0):
    #             user_prize += (total_prize/10)*2
    # return f'{str(user_prize)}'



if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)
