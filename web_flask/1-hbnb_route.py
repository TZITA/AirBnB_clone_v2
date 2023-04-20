#!/usr/bin/python3
"""
    A python script that starts a Flask web app
    that is listening on 0.0.0.0, port 5000.
    Routes:
        1. / : displays Hello HBNB!
        2. /hbtn : displays HBNB
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_h():
    """ Displays HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
