from string import ascii_letters

from flask import Response, make_response, render_template, request
from flask_restx import Namespace, Resource

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
            if not set(text) <= set(ascii_letters + " "):
                return Response(
                    response="В поле 'текст' могут быть только латинские символы <a href='/ciphre/caeaser/'>попробовать еще раз</a>",
                    status=400,
                )
            shift = int(request.form.get("shift"))
        except:
            return Response(
                response="Вы ввели не число в поле 'сдвиг по алфавиту'<br>или не текст в поле 'текст' <a href='/ciphre/caeaser/'>попробовать еще раз</a>",
                status=400,
            )
        return Response(
            response="<h1>Результат: {}".format(caeser_cipher(text, shift)),
            status=200,
        )
