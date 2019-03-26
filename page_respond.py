from flask import Blueprint, render_template, request, session
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

@bp.route("/vote", methods = ("GET", "POST"))
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

        if poll.id() in session:
            return render_error("You already submitted a response for this poll.")

        if not pdb.add_response(poll.id(), choice):
            return render_error("An error occurred trying to submit your response for the poll, please try again.")

        session[poll.id()] = True
        # to do: redirect to results page with success message

    return render_template("vote.html",
        id = poll.id(), question = poll.question(), choices = poll.choices()
    )

@bp.route("/results")
def results():
    poll = get_poll()
    if not poll:
        return render_error()

    return render_template("results.html", 
        question = poll.question(), choices = poll.choices(), responses = poll.responses(),
        sum = sum, round = round, int = int
    )