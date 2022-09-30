from project.backend.dao.user import UserDao
from project.backend.service.auth import AuthService
from project.backend.service.user import UserService
from project.backend.setup_db import db


user_dao = UserDao(db.session)

user_service = UserService(user_dao)
auth_service = AuthService(user_dao)
