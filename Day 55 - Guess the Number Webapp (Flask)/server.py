from flask import Flask
import random

app = Flask(__name__)

number_to_guess = 0


@app.route("/")
def homepage():
    global number_to_guess
    number_to_guess = random.randint(0, 9)
    return "<h1 style='text-align:center;font-weight: bold;'>Guess a number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='margin:auto; display:block;'>"


@app.route("/<int:guessed_number>")
def check_answer(guessed_number):
    if guessed_number == number_to_guess:
        return "<h1 style='text-align:center;font-weight: bold;'>You found me!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style='margin:auto; display:block;'>"

    elif guessed_number < number_to_guess:
        return "<h1 style='text-align:center;font-weight: bold;'>Too Low, Guess Higher!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' style='margin:auto; display:block;'>"

    else:
        return "<h1 style='text-align:center;font-weight: bold;'>Too High, Guess Lower!</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style='margin:auto; display:block;'>"


app.run(debug=True)
