import logging
from importlib import import_module

from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from app.config import DebugConfig

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

db = MongoEngine()
appbuilder = AppBuilder(security_manager_class=SecurityManager)
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    appbuilder.init_app(app, session=None)
    login_manager.init_app(app)



def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
    pass


def create_app(config):
# def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # app.config.from_object(DebugConfig())
    register_extensions(app)
    register_blueprints(app)

    return app


