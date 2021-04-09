from flask import Flask, render_template, jsonify
import random as rand

app = Flask(__name__)


@app.route("/randomnum")
def randomnum():
    account_number = ""
    for number in range(8):
        random_number = str(rand.randint(0,9))
        account_number += random_number
    return f'{account_number}'
print(randomnum(),end="")

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)

