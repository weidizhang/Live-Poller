from flask import Blueprint, render_template, request

bp = Blueprint("respond", __name__, url_prefix = "/respond")

@bp.route("/vote", methods=("GET", "POST"))
def respond():
    poll_id = request.args.get("id")

    error = False
    if poll_id:
        try:
            poll_id = int(poll_id)
        except ValueError:
            error = True

        # check if valid poll id
        print(poll_id)
        # todo
    else:
        error = True

    if error:
        return render_template("error.html", message = "The poll you are trying to vote on was not found.")

    if request.method == "POST":
        pass

    return render_template("respond.html")

@bp.route("/results")
def results():
    pass