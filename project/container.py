from project.dao.auth import AuthDao
from project.service.auth import AuthService
from project.setup_db import db

auth_dao = AuthDao(db.session)


auth_service = AuthService(auth_dao)
