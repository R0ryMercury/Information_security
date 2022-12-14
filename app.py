from flask import Flask, redirect, send_from_directory
from flask_restx import Api

from project.backend.config import Config
from project.backend.constants import UPLOAD_FOLDER
from project.backend.create_data import init_db
from project.backend.setup_db import db
from project.backend.views.auth.auth import auth_ns
from project.backend.views.auth.user import user_ns
from project.backend.views.ciphre.ciphre import ciphre_ns
from project.backend.views.main.main import main_ns
from project.backend.views.steganography.steganography import stegano_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(
        __name__,
        template_folder="project/frontend/templates",
        static_folder="project/frontend/static",
    )
    app.config.from_object(config_object)

    @app.route("/")
    def index():
        return redirect("/main/")

    @app.route("/uploads/<path:path>")
    def static_dir(path):
        return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)

    register_extensions(app)
    return app


# функция подключения расширений
def register_extensions(app):
    db.init_app(app)
    api = Api(app, title="Flask Api", doc="/docs")
    api.add_namespace(main_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(ciphre_ns)
    api.add_namespace(stegano_ns)


app = create_app(Config())

with app.app_context():
    db.create_all()
    # init_db()


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
