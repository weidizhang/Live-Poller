import os

from flask import Flask
from . import respond

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    #app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile("config.py", silent = True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    define_routes(app)
    return app

def define_routes(app):
    app.register_blueprint(respond.bp)