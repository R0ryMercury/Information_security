from flask import render_template, make_response
from flask_restx import Namespace, Resource
from project.dao.models.user import User, UserSchema
from project.helpers import auth_required

main_ns = Namespace("main")


@main_ns.route("/")
class MainView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("main.html"), 200, headers)
