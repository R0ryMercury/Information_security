from project.dao.user import UserDao
from project.service.auth import AuthService
from project.service.user import UserService
from project.setup_db import db


user_dao = UserDao(db.session)

user_service = UserService(user_dao)
auth_service = AuthService(user_dao)
