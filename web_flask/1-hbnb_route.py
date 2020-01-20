#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Function called with /hbnb route """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
