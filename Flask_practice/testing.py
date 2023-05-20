#!/usr/bin/python3
import sys
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Configure the MySQL database connection
url = ('mysql://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]))

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

# Define the model class
Base = declarative_base()

class Test(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Route to display data
@app.route('/')
def display_data():
    data = session.query(Test).all()
    return render_template('storage.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
