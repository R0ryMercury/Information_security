from project.dao.user import UserDao
from project.service.auth import AuthService
from project.setup_db import db

auth_dao = UserDao(db.session)


auth_service = AuthService(auth_dao)
