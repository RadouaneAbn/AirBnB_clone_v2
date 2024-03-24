#!/usr/bin/python3
"""
    This model starts a Flask web application
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


def get_db(cls=None):
    """ This function returns data from storage db/fs """
    return storage.all(cls)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ This function closes the current SQLAlchemy Session """
    storage.close()


@app.route("/", strict_slashes=False)
def home():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def greet_c(text):
    """Route to display 'C ' followed by string"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def greet_python(text="is cool"):
    """Route to display 'python ' followed by a string"""
    return "python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """Route to display '<n> is a number' if n is a number"""
    if n.isdigit():
        return "{} is a Number".format(n)
    else:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def display_number(n):
    """Route to display number using a template."""
    if n.isdigit():
        return render_template("5-number.html", number=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def display_number_type(n):
    """Route to display if the number is odd or even using a template"""
    if n.isdigit():
        type_n = "even" if int(n) % 2 == 0 else "odd"
        return render_template("6-number_odd_or_even.html",
                               number=n, type_n=type_n)
    else:
        abort(404)


@app.route("/states_list")
def states_list():
    """ This function displays an HTML page """
    state_insts = get_db(State).values()
    state_insts = sorted(state_insts, key=lambda state: state.name)
    return render_template("7-states_list.html",
                           states=state_insts)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
