from flask import render_template, request, redirect, url_for
from flask_restx import Namespace, Resource
from project.container import auth_service

check_ns = Namespace("check")


@check_ns.route("/login")
class CheckViewLogin(Resource):
    def get(self):
        req_form = request.form.to_dict(flat=False)
        if token := req_form.get("token"):
            user_d = auth_service.check_token(token)
            return redirect(url_for("user/profile"), user_d=user_d)
        if (username := req_form.get("username")) and (
            password := req_form.get("password")
        ):

            user_d = auth_service.check_user(username, password)
            return redirect(url_for("user/profile"), user_d=user_d)


@check_ns.route("/register")
class CheckViewRegister(Resource):
    def get(self):
        pass
