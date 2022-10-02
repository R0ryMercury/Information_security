from flask_restx import Namespace, Resource
from flask import render_template, make_response

from project.backend.helpers import auth_required

ciphre_ns = Namespace("ciphre")


@ciphre_ns.route("/caeaser/")
class CaeaserView(Resource):
    @auth_required
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("caeaser_ciphre.html"), 200, headers)
    @auth_required
    def post(self):
        