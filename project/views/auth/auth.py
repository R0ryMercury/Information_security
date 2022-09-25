from flask import render_template, make_response
from flask_restx import Namespace, Resource

auth_ns = Namespace("auth")


@auth_ns.route("/register/")
class RegisterView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("register.html"), 200, headers)


@auth_ns.route("/login/")
class LoginView(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("auth.html"), 200, headers)
