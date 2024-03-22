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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
