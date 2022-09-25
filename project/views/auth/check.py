from flask import render_template, request, redirect, url_for
from flask_restx import Namespace, Resource
from project.container import auth_service

check_ns = Namespace("check")


class CheckView(Resource):
    def get(self):
        req_form = request.form.to_dict(flat=False)
        if token := req_form.get("token"):
            user_d = auth_service.check_token(token)
            return redirect(url_for("user/profile"), user_d=user_d)
        if (username:= req_form.get("username")) and (password:=req_form.get("password")):
            