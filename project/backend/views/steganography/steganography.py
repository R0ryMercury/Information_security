from flask_restx import Resource, Namespace
from flask import redirect, flash, request, render_template
import os
from project.backend.ciphres.steganography import image_encode

from project.backend.constants import ALLOWED_EXTENSIONS

stegano_ns = Namespace("steganography")


@stegano_ns.route("/encode/")
class EncodeView(Resource):
    def get(self):
        return render_template("upload.html")

    def post(self):
        picture = request.files.get("picture")
        message = request.form.get("content")

        if not picture or not message:
            flash("Отсутствует картинка или текст")
            return redirect(request.url)
        if picture.filename.split(".")[-1] not in ALLOWED_EXTENSIONS:
            flash("Недопустимый формат картинки")
            return redirect(request.url)

        try:
            result = image_encode(picture.filename, message)
        except FileNotFoundError:
            flash("Файл не найден")
            return redirect(request.url)
        return render_template("uploaded.html", pic=result)
