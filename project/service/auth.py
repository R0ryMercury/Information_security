from flask import abort
from project.dao.auth import AuthDao
from project.helpers import encode_token


class AuthService:
    def __init__(self, dao: AuthDao) -> None:
        self.dao = dao

    def check_token(self, token):
        if data := encode_token(token):
            return data.get("name")
        abort(401)
    def check_user(self, username, password):
        if 