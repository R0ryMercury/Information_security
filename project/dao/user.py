from project.dao.models.user import User
from datetime import datetime


class UserDao:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user_d):
        ent = User(
            username=user_d.get("username"),
            email=user_d.get("email"),
            password= user_d.get("password"),
            first_name=user_d.get("first_name"),
            last_name=user_d.get("last_name"),
            job=user_d.get("job"),
            company=user_d.get("company"),
            address=user_d.get("address"),
            birthdate=datetime.strptime(user_d.get("birthdate"), "%d.%m.%Y"),
        )
        self.session.add(ent)
        self.session.commit()

    def get_user(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
