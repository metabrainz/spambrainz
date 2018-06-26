from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import PasswordType, force_auto_coercion

db = SQLAlchemy()

force_auto_coercion()
Base = declarative_base()


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


def reset_debug_db():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(User("admin", "adminPassword"))
    db.session.commit()
