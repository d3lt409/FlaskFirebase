from flask_login import current_user
from app.firebase_db import delete_todo
from flask import redirect, url_for

from . import todo_bp

@todo_bp.route("/todo/delete/<todo_id>", methods=['POST'])
def delete(todo_id):
    user = current_user
    delete_todo(user.id, todo_id)
    return redirect(url_for('home.home'))