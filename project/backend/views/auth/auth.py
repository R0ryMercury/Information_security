from flask import render_template, make_response, request, abort, redirect, Response
from flask_restx import Namespace, Resource
from project.backend.container import user_service
from project.backend.helpers import generate_tokens

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class RegisterView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("register.html"), 200, headers)

    def post(self):
        if req_data := request.form.to_dict():
            try:
                user_service.create(req_data)
                return redirect("/auth/login", code=302)
            except:
                return Response(
                    response="Одно из полей указано неверно <a href='/auth/register/'>попробовать еще раз</a>",
                    status=400,
                )
        return "что-то пошло не так, го дебажить"


@auth_ns.route("/login/")
class LoginView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("auth.html"), 200, headers)

    def post(self):
        if req_data := request.form.to_dict():
            tokens = generate_tokens(req_data)

            if req_data := request.form.to_dict():
                if user_d := user_service.get_user(req_data.get("username")):
                    headers = {
                        "Content-Type": "text/html",
                        "Authorization": f"Bearer {tokens.get('access_token')}",
                    }
                    return make_response(
                        render_template("profile.html", user=user_d), 200, headers
                    )
