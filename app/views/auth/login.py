from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user

from app.models.userModel import User, UserData
from app.firebase_db import get_user_by_username
from app.views.form import LoginForm
from werkzeug.security import check_password_hash

from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    loging_form = LoginForm()
    if loging_form.validate_on_submit():
        username = loging_form.username.data.lower()
        password = loging_form.password.data
        user_doc = get_user_by_username(username)
        user = user_doc.to_dict() if user_doc else None
        if user_doc and check_password_hash(user["password"],password):
            
            user["id"] = user_doc.id
            user_model = User(UserData(**user))
            login_user(user_model)
            flash(
                f"Bienvenido usuario {user['username'].capitalize()}", "success")
            return redirect(url_for("home.home"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    context = {
        "login_form": loging_form,
        "username": session.get("username")
    }

    return render_template("login.html", **context)
