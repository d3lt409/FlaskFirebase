import warnings, os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

from .config import DevelopmentConfig
from flask_fontawesome import FontAwesome
from flask_login import LoginManager

from .views import home_bp,  main_bp, auth_bp, todo_bp
from .models.userModel import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query(user_id)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    bootstrap =  Bootstrap4(app)
    frontawesome = FontAwesome(app)
    app.config.from_object(DevelopmentConfig)
    
    login_manager.init_app(app)
    
    
    app.register_blueprint(home_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404_error.html", error=error)


    warnings.simplefilter("ignore", ResourceWarning)

    return app