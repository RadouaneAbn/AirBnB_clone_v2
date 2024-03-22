#!/usr/bin/python3
"""
This module starts a Flask web application
"""

from flask import Flask, abort, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
