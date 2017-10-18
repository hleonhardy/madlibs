"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Form for madlib game"""

    answer = request.args.get("game")

    if answer == 'no':
        return render_template("goodbye.html")

    return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    noun2 = request.args.get("noun2")
    adjective = request.args.get("adj")
    noun = request.args.get("noun")
    adjective2 = request.args.get("adj2")
    verb = request.args.get("verb")
    pronoun = request.args.get("pro")

    return render_template("madlib.html",
                            noun2=noun2,
                            adjective2=adjective2,
                            noun=noun,
                            adjective=adjective,
                            pronoun=pronoun.title(),
                            verb=verb)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
