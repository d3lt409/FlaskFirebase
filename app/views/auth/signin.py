from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash

from app.models.userModel import User, UserData
from app.firebase_db import get_user_by_username, generate_auto_increment_id, create_user
from app.views.form import LoginForm

from . import auth_bp


@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():

    loging_form = LoginForm()
    if loging_form.validate_on_submit():
        user_post = loging_form.data
        user_db = get_user_by_username(user_post["username"].lower())
        if user_db:
            flash(f"Usuario con username {user_post['username']} ya existe", "warning")
            return redirect(url_for("auth.signin"))
        else:
            username = user_post["username"]
            password = user_post["password"]
            id = generate_auto_increment_id("users")
            user_data = UserData(id=id, username=username, password=generate_password_hash(password))
            create_user(user_data)
            login_user(User(user_data))
            return redirect(url_for("home.home",))
    context = {
        "signin_form": loging_form
    }

    return render_template("signin.html", **context)
