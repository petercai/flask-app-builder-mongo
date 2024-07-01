import logging
from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# app = Flask(__name__)
# app.config.from_object('config')
db = MongoEngine()
appbuilder = AppBuilder(security_manager_class=SecurityManager)



def register_extensions(app):
    db.init_app(app)
    appbuilder.init_app(app, session=None)
    # login_manager.init_app(app)



def register_blueprints(app):
    # for module_name in ('authentication', 'accp', 'home', 'api'):
    #     module = import_module('apps.{}.routes'.format(module_name))
    #     app.register_blueprint(module.blueprint)
    pass


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # app.config["MONGODB_SETTINGS"] = [
    #     {
    #         "db": "accp",
    #         "host": "localhost",
    #         "port": 27017,
    #         "alias": "default",
    #     }
    # ]
    register_extensions(app)
    register_blueprints(app)

    # app.register_blueprint(github_blueprint, url_prefix="/login") 
    
    # configure_database(app)
    return app
   

# from app import views

