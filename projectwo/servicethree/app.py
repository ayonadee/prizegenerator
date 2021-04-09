from flask import Flask, render_template, jsonify
import random as rand
import string

app = Flask(__name__)


@app.route("/randomletter")
def randomletter():
    random_letter = ""
    lower_alphabet = string.ascii_letters.lower()
    for letter in range(0,4):
        random_letter += rand.choice(lower_alphabet)
    return f'{random_letter}'
print(randomletter(), end="")

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)
