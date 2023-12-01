#!/usr/bin/python3
"""starts the pathway web application"""
from models import storage
from models.user import User
from models.parcel import Parcel
from models.review import Review
from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current sqlalchemy session"""
    storage.close()


@app.route('/', strict_slashes=False)
def pathway():
    """pathway web app"""









if __name__ == '__main__':
    app.run(host='0.0.0.0', ports=5000)
