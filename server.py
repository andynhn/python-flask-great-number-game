# By Andy Nguyen
# Great Number Game Assignment - Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(1,101)
        print(f"NEW GAME: The number for this new game is: {session['number']}")
    else:
        print(f"The number I am thinking of is: {session['number']}")
    return render_template("index.html")

@app.route('/verify', methods=['POST'])
def verify():
    print(request.form)
    if int(session['number']) > int(request.form['guess']):
        session['reply'] = 'low'
        session['color'] = "darkred"
        print("guess is too low")

    if int(session['number']) < int(request.form['guess']):
        session['reply'] = 'high'
        session['color'] = "darkred"
        print("guess is too high")

    if int(session['number']) == int(request.form['guess']):
        session['status'] = 'gameover'
        session['reply'] = 'correct'
        session['color'] = 'darkgreen'
        print("guess is correct!")

    return redirect('/')

@app.route('/reset')
def reset():
    print("Session data is about to be reset.")
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)