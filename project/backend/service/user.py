from project.backend.dao.user import UserDao
from project.backend.helpers import generate_tokens, get_hashed_password


class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def get_user(self, username):
        return self.dao.get_user(username)

    def create(self, user_d):
        user_d["password"] = get_hashed_password(user_d.get("password").encode())
        self.dao.create(user_d)

    def create_tokens(self, user_d):
        return generate_tokens(
            {
                "username": user_d.username,
                "email": user_d.email,
                "password": user_d.password,
                "role": user_d.role
            }
        )
