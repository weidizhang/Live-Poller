from flask import Blueprint, render_template, request, redirect, url_for
from . import page_manage

bp = Blueprint("index", __name__, url_prefix = "/")

@bp.route("/")
def index():
    if page_manage.can_manage():
        return redirect(url_for("manage.index"))

    return render_template("error.html", message = "There is nothing here to be displayed.")