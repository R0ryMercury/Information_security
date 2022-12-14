from flask import make_response, render_template, request, send_file
from flask_restx import Namespace, Resource

from project.backend.ciphres.steganography import image_decode, image_encode
from project.backend.constants import ALLOWED_EXTENSIONS
from project.backend.helpers import auth_required, save_pic

stegano_ns = Namespace("steganography")


@stegano_ns.route("/encode/")
class EncodeView(Resource):
    @auth_required
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("upload_encode.html"), 200, headers)

    @auth_required
    def post(self):
        picture = request.files.get("picture")
        message = request.form.get("message")

        if not picture or not message:
            return "Отсутствует картинка или текст"
        if picture.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
            return "Недопустимый формат картинки"

        try:
            path = save_pic(picture)
            result = image_encode(path, message)
        except FileNotFoundError:
            return "Файл не найден"
        return send_file(result)


@stegano_ns.route("/decode/")
class DecodeView(Resource):
    @auth_required
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("upload_decode.html"), 200, headers)

    @auth_required
    def post(self):
        picture = request.files.get("picture")

        if not picture:
            return "Отсутствует картинка"
        if picture.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
            return "Недопустимый формат картинки"

        try:
            path = save_pic(picture)
            result = image_decode(path)
        except FileNotFoundError:
            return "Файл не найден"
        except ValueError:
            return "Оригинальная картинка была не в jpg, зашифруйте заново"
        return f"Результат расшифровки: {result}"
