from flask import abort
from project.backend.dao.user import UserDao
from project.backend.helpers import check_password, encode_token


class AuthService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def check_token(self, token):
        if data := encode_token(token):
            return data.get("name")
        abort(401)

    def check_user(self, username, password):
        user = self.dao.get_user(username)
        if check_password(password, user.password):
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "job": user.job,
                "company": user.company,
                "address": user.address,
                "birthdate": user.birthdate,
            }
        abort(401)
