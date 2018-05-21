from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import PasswordType, force_auto_coercion
from .base import Base

force_auto_coercion()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(PasswordType(schemes=["pbkdf2_sha512"]), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username
