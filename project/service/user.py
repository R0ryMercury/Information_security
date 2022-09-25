from flask_restx import Namespace, Resource
from flask import request, render_template, make_response

user_ns = Namespace("user")


@user_ns.route("/profile")
class UserProfile(Resource):
    def get(self):
        user_d = request.args.get("user_d")
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("profile.html", user=user_d), 200, headers)
