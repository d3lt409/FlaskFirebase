from flask_login import current_user
from app.firebase_db import update_todo
from flask import redirect, url_for

from . import todo_bp

@todo_bp.route("/todo/update/<todo_id>/<done>", methods=['POST'])
def update(todo_id, done):
    user = current_user
    update_todo(user.id, todo_id, eval(done))
    
    return redirect(url_for('home.home'))