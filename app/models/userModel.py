from flask_login import UserMixin
from app.firebase_db import get_user


class UserData:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class User(UserMixin):
    """User Model Login Manager

    Args:
        UserMixin (UserMixin): Inherited from flask_login
    """

    def __init__(self, user_data: UserData):
        self.id = user_data.id
        self.username = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user = user_doc.to_dict()
        user["id"] = user_doc.id
        user_data = UserData(**user)

        return User(user_data)
    
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active
    
    
    