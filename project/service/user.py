from project.dao.user import UserDao
from project.helpers import get_hashed_password


class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def get_user(self, username):
        return self.dao.get_user(username)

    def create(self, user_d):
        user_d["password"] = get_hashed_password(user_d.get("password"))
        self.dao.create(user_d)
