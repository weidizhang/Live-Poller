import os

from flask import Flask
from datetime import datetime

from . import config, page_index, page_respond, page_manage

def create_app():
    app = Flask(__name__)

    define_routes(app)
    define_filters(app)
    return app

def define_routes(app):
    app.register_blueprint(page_index.bp)
    app.register_blueprint(page_respond.bp)
    app.register_blueprint(page_manage.bp)

def define_filters(app):    
    @app.template_filter()
    def format_timestamp(ts):
        return datetime.fromtimestamp(ts).strftime(config.settings["time_format"])