from flask import Blueprint, render_template, request

bp = Blueprint("respond", __name__, url_prefix = "/respond")

def get_poll_id():
    poll_id = request.args.get("id")
    if poll_id:
        # check it is valid
        return poll_id
    return False

def render_error(msg = "The poll you are trying to vote on was not found."):
    return render_template("error.html", message = msg)

@bp.route("/vote", methods=("GET", "POST"))
def respond():
    poll_id = get_poll_id()
    if not poll_id:
        return render_error()

    if request.method == "POST":
        pass

    return render_template("respond.html")

@bp.route("/results")
def results():
    poll_id = get_poll_id()
    if not poll_id:
        return render_error()

    # generate results