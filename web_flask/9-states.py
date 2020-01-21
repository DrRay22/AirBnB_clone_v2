#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_html(id=None):
    """ Function called with /states route """
    states = storage.all(State).values()

    if not id:
        return render_template('9-states.html',
                               Table="States",
                               items=states)

    for state in states:
        if state.id == id:
            return render_template('9-states.html',
                                   Table="State: {}".format(state.name),
                                   items=state.cities)

    return render_template('9-states.html',
                           items=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
