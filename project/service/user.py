from project.dao.user import UserDao


class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.dao = dao

    def get_user(self, username):
        return self.dao.get_user(username)

    def create(self, user_d):
        self.dao.create(user_d)
