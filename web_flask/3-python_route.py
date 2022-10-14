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


@app.route('/c/<text>')
def display_c_input(input):
    """Method to display C + the input text"""
    return 'C %s' % input.replace("_", " ")


@app.route('/python')
@app.route('/python/<p_text>')
def display_python_input(p_input='is cool'):
    """Method to display Python + the input text"""
    return 'Python %s' % p_text.replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
