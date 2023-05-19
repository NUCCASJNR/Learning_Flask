#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about/',  strict_slashes=False)
def about():
    return 'About page'
@app.route('/user/<user>')
def show_user(user):
    return f'This is User: {user}'
@app.route('/age/<aged>')
def show_Age(aged):
    return f'you are {aged} years old'
@app.route('/state/<states>')
def state(states):
    return f'Your from {states}'
@app.route('/email/<email>')
def email(email):
    return f'Your email address is : {email}'
