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
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
