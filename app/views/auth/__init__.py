from flask import Blueprint

auth_bp = Blueprint("auth", __name__, static_url_path='/auth')

from .login import login
from .logout import logout
from .signin import signin