from flask import make_response, render_template, session
from flask_restx import Namespace, Resource

main_ns = Namespace("main")


@main_ns.route("/")
class MainView(Resource):
    def get(self):
        session.pop("token", None)
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("main.html"), 200, headers)
