#!/usr/bin/python3
"""
    This model starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def get_db(cls=None):
    """ This function returns data from storage db/fs """
    return storage.all(cls)


@app.teardown_appcontext
def teardown_db(exception):
    """ This function closes the current SQLAlchemy Session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ This function displays an HTML page """
    from models.state import State
    return render_template("7-states_list.html",
                           list_state_inst=get_db(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
