from flask_restx import Namespace, Resource
from flask import request, render_template, make_response, abort

user_ns = Namespace("user")


@user_ns.route("/get_token")
class UserView(Resource):
    def get(self):
        pass


@user_ns.route("/profile")
class UserProfile(Resource):
    def get(self):
        if user_d := request.args:
            headers = {"Content-Type": "text/html"}
            return make_response(
                render_template("profile.html", user=user_d), 200, headers
            )
        abort(401)
