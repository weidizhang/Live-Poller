from flask import Blueprint, render_template, request
from .page_respond import get_poll, render_error
from . import config

bp = Blueprint("share", __name__, url_prefix = "/share")

@bp.route("/")
def index():
    poll = get_poll()
    if not poll:
        return render_error("The poll you were shared was not found.", True)

    # Do it this way instead of using url_for in the jinja template because we want the generated
    # QR code iamge to have the correct domain that is accessible by the end user scanning it

    protocol, port = request.host_url.split(":")[0], request.host.split(":")[1]
    base_url = protocol + "://" + config.settings["base_domain"] + ":" + port + "/respond/vote?id="
    return render_template("share.html", base = base_url, poll = poll)