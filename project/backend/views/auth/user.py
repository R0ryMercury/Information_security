from flask_restx import Resource, Namespace
from flask import (
    request,
    render_template,
    session,
    make_response,
    render_template_string,
    Response,
)
from project.backend.helpers import auth_required, encode_token
from project.backend.container import user_service

user_ns = Namespace("user")


@user_ns.route("/profile/")
class UserProfile(Resource):
    @auth_required
    def get(self):
        token = session.get("token")
        user_d = encode_token(token)
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("profile.html", user=user_d), 200, headers)


@user_ns.route("/password/")
class UserPassword(Resource):
    @auth_required
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("pass_change.html"), 200, headers)

    @auth_required
    def post(self):
        passwords = request.form.to_dict()
        if user_service.update_password(passwords):
            return Response(
                response="Пароль успешно изменен <a href='/user/profile/'>вернуться в профиль</a>",
                status=200,
            )
        return Response(
            response="Одно из полей указано неверно <a href='/user/password/'>попробовать еще раз</a>",
            status=400,
        )
