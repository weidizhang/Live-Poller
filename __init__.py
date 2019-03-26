import os
import socket
import urllib.request

from flask import Flask
from flask_qrcode import QRcode
from datetime import datetime

from . import config, page_index, page_respond, page_manage, page_share

def create_app():
    app = Flask(__name__)
    app.secret_key = config.settings["secret_key"]

    update_config()
    define_routes(app)
    define_filters(app)
    QRcode(app)
    return app

def update_config():
    if not config.settings["base_domain"]:
        if config.settings["ran_locally"]:
            config.settings["base_domain"] = socket.gethostbyname(socket.gethostname())
        else:
            config.settings["base_domain"] = urllib.request.urlopen("https://api.ipify.org/").read().decode("utf8")

def define_routes(app):
    app.register_blueprint(page_index.bp)
    app.register_blueprint(page_respond.bp)
    app.register_blueprint(page_manage.bp)
    app.register_blueprint(page_share.bp)

def define_filters(app):
    @app.template_filter()
    def format_timestamp(ts):
        return datetime.fromtimestamp(ts).strftime(config.settings["time_format"])