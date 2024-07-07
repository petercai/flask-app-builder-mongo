import pytest
from flask import Flask
from flask_mongoengine import MongoEngine

from app.accp.models import Application


# from .models import Application

@pytest.fixture(scope="module")
def test_db_connection():
    # Set up a test MongoDB connection
    app = Flask(__name__)

    app.config['MONGODB_SETTINGS'] = {
        'db': 'portal',
        'host': 'localhost',
        'port': 27017
    }
    app.config['TESTING'] = True
    db = MongoEngine(app)
    yield db
def test_read_application_data(test_db_connection):


    # Read the data from the database
    all_apps = Application.objects.all()
    # iterate all_apps and print the name and project
    for app in all_apps:
        print(app._id, app.name, app.project)

    # Assert the data is correct
    # assert len(all_apps) == 13

