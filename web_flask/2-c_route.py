#!/usr/bin/python3
"""
    A python script that displays C followed by the value
    of the text variable.
    Underscores (_) are reolaced  with a space.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Displays C followed by the value of the text variable """
    text = text.split("_")
    text = " ".join(text)
    return "C %s" % text


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
