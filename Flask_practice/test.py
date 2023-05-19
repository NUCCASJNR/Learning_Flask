from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('test.html', utc_dt=datetime.now())

# ...
@app.route('/about/')
def about():
    return render_template('about.html')
