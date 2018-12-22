from flask import Blueprint, render_template, request
from .poll_db import PollDB

bp = Blueprint("respond", __name__, url_prefix = "/respond")
pdb = PollDB()

def get_poll():
    poll_id = request.args.get("id")
    if poll_id:
        poll = pdb.get_by_id(poll_id)
        if not poll.is_empty():
            return poll

    return False

def render_error(msg = "The poll you are trying to vote on was not found.", back = False):
    return render_template("error.html", message = msg, go_back = back)

@bp.route("/vote", methods=("GET", "POST"))
def vote():
    poll = get_poll()
    if not poll:
        return render_error()
    if poll.is_closed():
        pass # to do: redirect to results page

    if request.method == "POST":
        choice = request.form.get("choice")
        if not choice or not poll.is_valid_choice(choice):
            return render_error("You did not submit a valid response for the poll.", True)

        # process vote after session check

    return render_template("respond.html",
        id = poll.id(), question = poll.question(), choices = poll.choices(), enumerate = enumerate
    )

@bp.route("/results")
def results():
    poll = get_poll()
    if not poll:
        return render_error()

    # generate results