from flask import Flask, render_template
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

# @app.route("/randomletter")
# def randomletter():
#     lower_alphabet = ["a","b","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     letters = rand.choices(lower_alphabet, k=4)
#     letterstr = ''.join(letters)
#     return f'{letterstr}'


if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)
