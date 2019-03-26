from flask import Blueprint, redirect, render_template, request, session, url_for
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
        return redirect(url_for("respond.results", id = poll.id(), closed = 1))

    if request.method == "POST":
        choice = request.form.get("choice")
        if not choice or not poll.is_valid_choice(choice):
            return render_error("You did not submit a valid response for the poll.", True)

        if poll.id() in session:
            return redirect(url_for("respond.results", id = poll.id(), already_voted = 1))

        if not pdb.add_response(poll.id(), choice):
            return render_error("An error occurred trying to submit your response for the poll, please try again.", True)

        session[poll.id()] = True
        return redirect(url_for("respond.results", id = poll.id(), success = 1))

    return render_template("vote.html",
        id = poll.id(), question = poll.question(), choices = poll.choices()
    )

@bp.route("/results")
def results():
    poll = get_poll()
    if not poll:
        return render_error()

    return render_template("results.html", 
        question = poll.question(), choices = poll.choices(), responses = poll.responses(), closes = poll.closes(),
        sum = sum, round = round, int = int,
        success = request.args.get("success"),
        already_voted = request.args.get("already_voted"),
        closed = request.args.get("closed")
    )