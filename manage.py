from flask import Blueprint, render_template, request

bp = Blueprint("manage", __name__, url_prefix = "/manage")

def can_manage():
    return False

@bp.route("/")
def index():
    return render_template("manage.html")