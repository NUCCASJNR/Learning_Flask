#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Home Page'
    greeting = 'Sideeq whats popping'
    idan = 'how far idan'
    return render_template('subfolder/index.html', title=title, greeting=greeting, idan=idan)
