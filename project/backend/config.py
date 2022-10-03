import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "249y823r9v8238r9u"
    TESTING = False

    JSON_AS_ASCII = False
    RESTX_JSON = {
        "ensure_ascii": False,
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(BaseConfig):
    STRICT_SLASHES = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "users.db")
    UPLOAD_FOLDER = "/project/frontend/static/uploads"
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
