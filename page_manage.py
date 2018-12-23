from flask import Blueprint, render_template, request, abort
from . import config
from .poll_db import PollDB

bp = Blueprint("manage", __name__, url_prefix = "/manage")
pdb = PollDB()

def can_manage():
    return request.remote_addr in config.settings["manage_ip_addresses"]

def verify_can_manage():
    if not can_manage():
        abort(403)

@bp.route("/")
def index():
    verify_can_manage()

    all_polls = pdb.get_all()
    return render_template("manage.html", polls = all_polls)

@bp.route("/action", methods = ("POST",))
def action():
    verify_can_manage()

    valid_actions = ["create", "close", "delete"]
