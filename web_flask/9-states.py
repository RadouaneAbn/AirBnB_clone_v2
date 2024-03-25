#!/usr/bin/python3
"""
    This model starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


def get_db(cls=None):
    """ This function returns data from storage db/fs """
    return storage.all(cls).values()


@app.teardown_appcontext
def teardown_db(exception=None):
    """ This function closes the current SQLAlchemy Session """
    storage.close()


@app.route("/states_list")
def states_list():
    """ This function displays an HTML page """
    state_insts = get_db(State)
    state_insts = sorted(state_insts, key=lambda state: state.name)
    return render_template("7-states_list.html",
                           states=state_insts)


@app.route("/cities_by_states")
def cities_by_states():
    """ This function displays an HTML page """
    state_insts = get_db(State)
    return render_template("8-cities_by_states.html",
                           states=state_insts)


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """ This function all states or all cities in a state
        if an id is given
    """
    if id:
        states = storage.all(State).get(f"State.{id}", None)
    else:
        states = get_db(State)
    return render_template("9-states.html", states=states,
                           id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
