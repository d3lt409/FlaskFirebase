import unittest
from flask_testing import TestCase
from flask import current_app, url_for
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .. import create_app

class TestFlask(TestCase):
    
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config["TESTING"])
        
    def test_index_redirects(self):
        response  = self.client.get(url_for("main.main"))
        self.assertTrue(response.status_code == 302 and  response.headers["Location"] == "/home")
        
    def test_hello_get(self):
        response  = self.client.get(url_for("home.home"))
        self.assert200(response)
        
    def test_auth_login_post(self):
        response  = self.client.post(url_for("auth.login"), data={
            "username":"fake",
            "password":"fake_password"
        })
        self.assertTrue(response.status_code == 302 and  response.headers["Location"] == "/")
        
    def test_auth_blueprint(self):
        self.assertIn("auth", self.app.blueprints)
        
    def test_login_get(self):
        response = self.client.get(url_for("auth.login"))
        self.assert200(response)
        
    def test_login_template(self):
        self.client.get(url_for("auth.login"))
        self.assert_template_used("login.html")
    
if __name__ == "__main__":
    unittest.main()