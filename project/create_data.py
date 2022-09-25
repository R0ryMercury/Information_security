from datetime import datetime
from secrets import choice
from faker import Faker
from project.dao.models.user import User
from project.helpers import get_hashed_password
from project.setup_db import db


def init_db():
    fake = Faker(["ru_RU"])
    with db.session.begin():
        if choice((0, 1)):
            db.session.add(
                User(
                    username=fake.unique.user_name(),
                    email=fake.unique.email(),
                    password=get_hashed_password(fake.password().encode()),
                    first_name=fake.first_name_male(),
                    last_name=fake.last_name_male(),
                    job=fake.job(),
                    company=fake.company(),
                    address=fake.address(),
                    birthdate=fake.date_of_birth(),
                )
            )
        else:
            db.session.add(
                User(
                    username=fake.unique.user_name(),
                    email=fake.unique.email(),
                    password=get_hashed_password(fake.password().encode()),
                    first_name=fake.first_name_female(),
                    last_name=fake.last_name_female(),
                    job=fake.job(),
                    company=fake.company(),
                    address=fake.address(),
                    birthdate=fake.date_between(),
                )
            )
