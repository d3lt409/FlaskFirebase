from flask import redirect, flash, url_for
from flask_login import logout_user, login_required

from . import auth_bp


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Regresa pronto", "success")
    return redirect(url_for("auth.login"))
