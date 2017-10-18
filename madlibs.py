"""A madlib game that compliments its users."""

from random import choice, sample, randint

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

    compliments = sample(AWESOMENESS, randint(1, len(AWESOMENESS)))
    first = compliments[:-1]
    end = compliments[-1]
    compliments = ", ".join(first) + ", and " + end

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Form for madlib game"""

    answer = request.args.get("game")

    if answer == 'no':
        return render_template("goodbye.html")

    return render_template("game.html")


@app.route('/madlib', methods=["POST"])
def show_madlib():

    noun2 = request.form.get("noun2")
    adjective = request.form.get("adj")
    noun = request.form.get("noun")
    adjective2 = request.form.get("adj2")
    verb = request.form.get("verb")
    pronoun = request.form.get("pro")

    madlib_list = ["madlib.html", "madlib2.html"]
    which_madlib = choice(madlib_list)

    return render_template(which_madlib,
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
