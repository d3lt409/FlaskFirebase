from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.views.form import TodoForm, DeleteTodoForm, UpdateTodoForm

from app.firebase_db import get_todos, create_todo
from . import home_bp


@home_bp.route("/home", methods=["GET", "POST"])
@login_required
def home():
    todo_form = TodoForm()
    user_id = current_user.id
    if todo_form.validate_on_submit():
        todo = {
            "title": todo_form.data["title"],
            "description": todo_form.data["description"],
            "done": todo_form.data["done"]}
        create_todo(user_id, todo)
        flash(
            f"Task created!", "success")
        return redirect(url_for("home.home"))
    todos = get_todos(user_id)
    context = dict(todos=map(lambda x: {**x.to_dict(), "id": x.id}, todos),
                   username=current_user, todo_form=todo_form,
                   delete_todo_form=DeleteTodoForm(), update_form=UpdateTodoForm())

    return render_template("home.html", **context)
