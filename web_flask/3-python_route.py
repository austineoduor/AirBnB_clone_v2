#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Method to display the welcome text"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """Method to display the welcome text"""
    return 'HBNB'


@app.route('/c/<string:text>')
def display_c_input(text):
    """Method to display C + the input text"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python/', defaults={"text":"is cool"})
@app.route('/python/<string:text>')
def display_python_input(text):
    """Method to display Python + the input text"""
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
