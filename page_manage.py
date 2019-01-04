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

def handle_action(id, action):
    if id and action:
        poll = pdb.get_by_id(id)
        if poll.is_empty():
            return ("danger", "The poll you are trying to manage was not found.")
    
        generic_error = ("danger", "An error occurred trying to perform the specified action on the poll, please try again.")

        if action == "create":
            return ("info", "NOT YET IMPLEMENTED") # TODO
        elif action == "close":
            if poll.is_closed():
                return ("danger", "The poll you are trying to close is already closed.")
            return ("success", "The poll was successfully closed.") if pdb.close(poll.id()) else generic_error
        elif action == "delete":
            return ("success", "The poll was successfully deleted.") if pdb.delete(poll.id()) else generic_error
    
    return None

@bp.route("/", methods = ("GET", "POST"))
def index():
    verify_can_manage()

    msg = None
    if request.method == "POST":
        msg = handle_action(request.form.get("id"), request.form.get("action"))

    all_polls = pdb.get_all()
    return render_template("manage.html", message = msg, polls = all_polls)
