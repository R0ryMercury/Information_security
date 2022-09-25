from project.dao.models.user import User


class AuthDao:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()

    def get_user(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
