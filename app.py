from flask import Flask, redirect
from flask_restx import Api
from project.config import Config
from project.create_data import init_db
from project.views.main.main import main_ns
from project.views.auth.check import check_ns
from project.views.auth.user import user_ns
from project.views.auth.auth import auth_ns
from project.setup_db import db
from loguru import logger


# функция создания основного объекта app
def create_app(config_object):
    logger.add(
        "project/debug.log",
        format="{time} {level} {message}",
        level="DEBUG",
        rotation="10 KB",
        compression="zip",
    )
    app = Flask(
        __name__, template_folder="project/templates", static_folder="project/static"
    )
    app.static_folder = app.root_path + "/project/static"
    app.config.from_object(config_object)

    @app.route("/")
    def index():
        return redirect("/main/")

    register_extensions(app)

    return app


# функция подключения расширений
def register_extensions(app):
    db.init_app(app)
    api = Api(app, title="Flask Api", doc="/docs")
    api.add_namespace(main_ns)
    api.add_namespace(check_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


app = create_app(Config())

with app.app_context():
    init_db()


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
