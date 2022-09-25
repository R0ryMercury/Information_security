from flask import render_template
from flask_restx import Namespace, Resource
from project.dao.models.user import User, UserSchema
from project.helpers import auth_required

main_ns = Namespace("main")


@main_ns.route("/")
class MainView(Resource):
    def get(self):
        return render_template("index.html")
