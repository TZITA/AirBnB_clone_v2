#!/usr/bin/python3
"""
    A python script to start a flask web app
    that listens on 0.0.0.0 port 5000 and
    displays Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays Hello HBNB!."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
