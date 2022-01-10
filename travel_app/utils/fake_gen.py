from travel_app.database.config import settings
from travel_app.models import user
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

#assumes the table are already created

def gen_fake_user(n: int) -> None:
    fake_gen = Faker()

    for _ in range(n):
        fake_user = {
            "full_name": fake_gen.name(),
            "address": fake_gen.address(),
            "email": fake_gen.email(),
            "phone_no": fake_gen.phone_number(),
            "password": fake_gen.password()
        }
        session.add(user.User(**fake_user))
        session.commit()
