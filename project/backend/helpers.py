import base64
import calendar
import datetime
import hashlib
import hmac
import jwt
from flask import abort, session
from project.backend.constants import (
    JWT_ALGORITHM,
    JWT_SECRET,
    SALT,
    TOKEN_EXPIRE_DAYS,
    TOKEN_EXPIRE_MINUTES,
    UPLOAD_FOLDER,
)


def get_hashed_password(password):
    return base64.b64encode(hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 1000))


def check_password(password: str, hashed_password: str) -> bool:
    return hmac.compare_digest(
        base64.b64decode(hashed_password),
        hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 1000),
    )


def generate_tokens(data: dict) -> dict:
    minutes = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )
    data["exp"] = calendar.timegm(minutes.timetuple())
    access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    days = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
    data["exp"] = calendar.timegm(days.timetuple())
    refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def encode_token(token: str) -> dict:
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except Exception:
        return False
    return data


def auth_required(func):
    def wrapper(*args, **kwargs):
        if not (token := session.get("token")):
            abort(401)
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)
        return func(*args, *kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if not (token := session.get("token")):
            abort(401)
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if user.get("role") != "admin":
                abort(403)
        except Exception as e:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def save_pic(pic) -> str:
    """Функция сохраняет переданную ей картинку
    и возвращает путь до нее"""
    filename = pic.filename
    path = UPLOAD_FOLDER + f"/{filename}"
    pic.save(path)
    return path
