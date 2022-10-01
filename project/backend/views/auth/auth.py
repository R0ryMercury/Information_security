import json
from flask import (
    render_template,
    make_response,
    request,
    url_for,
    redirect,
    Response,
    session,
)
from flask_restx import Namespace, Resource
from project.backend.container import user_service
from project.backend.dao.models.user import UserSchema
from project.backend.helpers import generate_tokens

auth_ns = Namespace("auth")
user_schema = UserSchema()


@auth_ns.route("/register/")
class RegisterView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("register.html"), 200, headers)

    def post(self):
        if req_data := request.form.to_dict():
            try:
                user_service.create(req_data)
                return redirect("/auth/login/")
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
            if user_d := user_service.get_user(req_data.get("username")):
                user_string = user_schema.dumps(user_d)
                user_dict = json.loads(user_string)
                tokens = generate_tokens(user_dict)
                session["token"] = tokens.get("access_token")
                return redirect(url_for("user_user_profile"))
        return "Что-то пошло не так"
