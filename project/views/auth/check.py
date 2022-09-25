from flask import request, redirect, url_for, abort
from flask_restx import Namespace, Resource
from project.container import auth_service

check_ns = Namespace("check")


@check_ns.route("/login")
class CheckViewLogin(Resource):
    def get(self):
        req_data = request.args.to_dict(flat=False)
        if token := req_data.get("token"):
            user_d = auth_service.check_token(token)
            return redirect(url_for("user/profile"), user_d=user_d)
        if (username := req_data.get("username")) and (
            password := req_data.get("password")
        ):

            user_d = auth_service.check_user(username, password)
            return redirect(url_for("user.profile", user_d=user_d))
        abort(404)