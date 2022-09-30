from flask import abort
from project.backend.dao.user import UserDao
from project.backend.helpers import encode_token, generate_tokens


class AuthService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def check_token(self, token):
        if data := encode_token(token):
            return data.get("name")
        abort(401)

    def create_tokens(self, user_d):
        return generate_tokens(
            {
                "username": user_d.username,
                "email": user_d.email,
                "password": user_d.password,
                "role": user_d.role,
            }
        )
