from flask_restx import Namespace, Resource
from flask import request, render_template, make_response, abort, jsonify
from project.backend.container import user_service
from project.backend.helpers import generate_tokens

user_ns = Namespace("user")


@user_ns.route("/profile")
class UserProfile(Resource):
    def post(self):
        if req_data := request.form.to_dict():
            # tokens = generate_tokens(req_data)
            headers = {
                "Content-Type": "text/html",  # "Authorization": f"Bearer {tokens.get('access_token')}
            }
            if "email" in req_data:
                user_service.create(req_data)
                return make_response(
                    render_template("profile.html", user=req_data), 200, headers
                )
            elif user_d := user_service.get_user(req_data.get("username")):
                return make_response(
                    render_template("profile.html", user=user_d), 200, headers
                )
        abort(401)


# @user_ns.route("/password")
