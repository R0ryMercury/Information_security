from flask_restx import Resource, Namespace
from flask import request, render_template, session, make_response
from project.backend.helpers import auth_required, encode_token

user_ns = Namespace("user")


@user_ns.route("/profile")
class UserProfile(Resource):
    @auth_required
    def get(self):
        token = session.get("token")
        user_d = encode_token(token)
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("profile.html", user=user_d), 200, headers)
