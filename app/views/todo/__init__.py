from flask import Blueprint

todo_bp = Blueprint("todo", __name__, static_url_path='/todo')

from .delete import delete
from .update import update