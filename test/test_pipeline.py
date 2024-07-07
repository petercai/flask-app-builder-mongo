import pytest
from flask import Flask
from flask_mongoengine import MongoEngine

from app.pipeline.models import Application, Environment, Deployment


# from .models import Application

@pytest.fixture(scope="module")
def mongo_connection():
    # Set up a test MongoDB connection
    app = Flask(__name__)

    app.config['MONGODB_SETTINGS'] = {
        'db': 'portal',
        'host': 'localhost',
        'port': 27017
    }
    app.config['TESTING'] = True

    # The MongoEngine class is a wrapper around the PyMongo library, which provides a more Pythonic way of interacting
    # with MongoDB databases.
    # By passing the app object to the MongoEngine constructor,
    # it allows MongoEngine to access the application's configuration settings,
    # such as the MongoDB connection URI.
    db = MongoEngine(app)
    #  In Flask, it's common to use context managers or generators to create and manage resources (like database connections)
    #  that need to be initialized and torn down for each request.
    #  When this code is executed, it yields the db object,
    #  which is the initialized MongoEngine instance.
    #  This allows the caller (likely a Flask view function or a blueprint) to use the db
    #  object to interact with the MongoDB database within the context of the current request.
    #
    # After the caller is done using the db object, the context manager or generator function will be responsible for
    #  cleaning up or closing the database connection, if necessary.
    yield db

def test_read_application(mongo_connection):
    # Read the data from the database
    all_apps = Application.objects.all()
    # iterate all_apps and print the name and project
    for app in all_apps:
        print(app._id, app.name, app.project)

    # Assert the data is correct
    assert len(all_apps) == 13

def test_read_envs(mongo_connection):
    envs = Environment.objects.distinct("env")
    for env in envs:
        print(env)

def test_read_deployment(mongo_connection):
    deployments = Deployment.objects.all()
    for deployment in deployments:
        print(deployment._id, deployment.env, deployment.status, deployment.app.name, deployment.version,
              deployment.commit, deployment.deployer.name, deployment.start_time,
              deployment.end_time)
        # print(deployment)

def test_deployment_filter(mongo_connection):
    app = Application.objects(name='cdb-ux-authentication').first()
    deployments = Deployment.objects(env='PRD', app_id=app._id)
    for deployment in deployments:
        print(deployment._id, deployment.env, deployment.status, deployment.app.name, deployment.version,
              deployment.commit, deployment.deployer.name, deployment.start_time,
              deployment.end_time)