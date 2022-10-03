from flask_restx import Resource, Namespace
from flask import redirect, flash, request
import os

stegano_ns = Namespace("steganography")


@stegano_ns.route("/encode/")
class EncodeView(Resource):
    def get(self):
        pass

    # def post(self):
    #     if "file" not in request.files:
    #         flash("No file part")
    #         return redirect(request.url)
    #     file = request.files["file"]
    #     if file.filename == "":
    #         flash("No selected file")
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(, filename))
