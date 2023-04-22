#!/usr/bin/python3
"""
    A python script that displays a HTML page only if n is an integer.
    H1 tag: n is even|odd inside the tag BODY.
"""
from flask import Flask, render_template

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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def p_text(text):
    """ Displays Python followed by the value of the text variable """
    text = " ".join(text.split("_"))
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Displays n is a number if n is int."""
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_tem(n):
    """ Displays a HTML page only if n is an integer."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ Displays a HTML page only if n is an integer.
        H1 tag: Number: n is even|odd inside the tag BODY.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
