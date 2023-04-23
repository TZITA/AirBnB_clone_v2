#!/usr/bin/python3
"""
    A python script to start a flask web app:
        - listening on 0.0.0.0, port 5000
        - use storage to fetch data from storage engines
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """
    Displays a HTML page: (inside the tag BODY)
        - H1 tag: States
        - UL tag: list of all State objs in DBStorage sorted by name
            - LI tag: description of one State
                      + UL tag: with the list of City objs
                      linked to the State sorted by name
                - LI tag: description of one City
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
