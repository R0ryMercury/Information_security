from flask import render_template
from flask_restx import Namespace, Resource

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class RegisterView(Resource):
    def get(self):
        return render_template("register.html")


@auth_ns.route("/login")
class LoginView(Resource):
    def post(self):
        return render_template("login.html")
