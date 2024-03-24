#!/usr/bin/python3

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

def get_db():
    return storage.all()

app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html",
                           list_state_inst=get_db())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)