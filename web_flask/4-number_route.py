#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Method to display the welcome text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Method to display the welcome text"""
    return 'HBNB'


@app.route('/c/<input>', strict_slashes=False)
def display_c_input(text):
    """Method to display C + the input text"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<p_text>', strict_slashes=False)
def display_python_text(p_input='is cool'):
    """Method to display Python + the input text"""
    return 'Python %s' % p_text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Method to display "is a number" in case of input n being an int"""
    return '%d is a number' % n

if __name__ == "__main__":
    app.run(host='0.0.0.0')
