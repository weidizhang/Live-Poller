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
    if ((not id and action == "create") or id) and action:
        poll = None
        if id:
            poll = pdb.get_by_id(id)
            if poll.is_empty():
                return ("danger", "The poll you are trying to manage was not found.")

        generic_success = ("success", "The poll was successfully " + action + "d.")
        generic_error = ("danger", "An error occurred trying to perform the specified action on the poll, please try again.")

        if action == "create":
            question = request.form.get("question")
            responses = request.form.getlist("responses[]")
            closes = request.form.get("closes")

            if not question or not responses or not closes or len(responses) < 1:
                return ("danger", "One or more fields that are required to create a poll were not supplied.")

            return generic_success if pdb.create(question, closes, responses) else generic_error
        elif action == "close":
            if poll.is_closed():
                return ("danger", "The poll you are trying to close is already closed.")
            return generic_success if pdb.close(poll.id()) else generic_error
        elif action == "delete":
            return generic_success if pdb.delete(poll.id()) else generic_error
    
    return None

@bp.route("/", methods = ("GET", "POST"))
def index():
    verify_can_manage()

    msg = None
    if request.method == "POST":
        msg = handle_action(request.form.get("id"), request.form.get("action"))

    all_polls = pdb.get_all()
    return render_template("manage.html", message = msg, polls = all_polls)
