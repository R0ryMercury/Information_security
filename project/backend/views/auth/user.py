from flask_restx import Namespace, Resource
from flask import request, render_template, make_response, abort, jsonify
from project.backend.container import user_service
from project.backend.helpers import auth_required, encode_token, generate_tokens

user_ns = Namespace("user")


@user_ns.route("/profile")
class UserProfile(Resource):
    @auth_required
    def get(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        user_d = encode_token(token)
        return render_template("profile.html", user=user_d)


# @user_ns.route("/password")
