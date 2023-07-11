import os
from dotenv import load_dotenv

load_dotenv()
class Config(object):
    BOOTSTRAP_BOOTSWATCH_THEME = "darkly"

class DevelopmentConfig(Config):
    SECRET_KEY=os.environ.get("SECRET_KEY"),
    API_SECRET=os.environ.get("API_SECRET"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", None),
    FLASK_ENV=os.environ.get("ENV", "development"),
    DEBUG=True
    