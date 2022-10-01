from operator import itemgetter
from flask import session
from project.backend.dao.models.user import User
from project.backend.dao.user import UserDao
from project.backend.helpers import check_password, encode_token, get_hashed_password


class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def get_user(self, username: str) -> User:
        return self.dao.get_user(username)

    def create(self, user_d: dict) -> None:
        user_d["password"] = get_hashed_password(user_d.get("password"))
        user_d["role"] = "admin"
        self.dao.create(user_d)

    def update_password(self, passwords: dict) -> bool:
        old_password, new_password, new_password_repeated = itemgetter(
            "old_password", "new_password", "new_password_repeated"
        )(passwords)
        if new_password != new_password_repeated:
            return False
        if user_d := encode_token(session.get("token")):
            user = self.get_user(user_d.get("username"))
            if check_password(old_password, user.password):
                user.password = get_hashed_password(new_password)
                self.dao.update(user)
                return True
        return False
