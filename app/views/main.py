from flask import request, make_response, redirect, session, url_for
from flask.blueprints import Blueprint

main_bp = Blueprint('main', __name__)
@main_bp.route("/")
def main():
    user_ip = request.remote_addr
    session["user_ip"] = user_ip
    response =make_response(redirect(url_for("home.home")))
    
    return response