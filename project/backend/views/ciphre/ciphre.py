from flask_restx import Namespace, Resource
from flask import render_template, make_response, request, Response
from project.backend.ciphres.caeaser_ciphre import caeser_cipher
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
        text = request.form.get("text")
        try:
            shift = int(request.form.get("shift"))
        except:
            return Response(
                response="Вы ввели не число <a href='/ciphre/caeaser/'>попробовать еще раз</a>",
                status=400,
            )
        return Response(
            response="<h1>Результат: {}".format(caeser_cipher(text, shift)),
            status=200,
        )
