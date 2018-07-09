import os


class Config(object):
    DEBUG = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    THREADS_PER_PAGE = 2

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"

    SECRET_KEY = "secret"

    API_PREFIX = "/api/1.0"

    # Loaded from .env, do not modify
    SQLALCHEMY_DATABASE_URI = os.getenv("SB_DATABASE_URI")
    MB_DATABASE_URI = os.getenv("MB_DATABASE_URI")
    BACKEND = os.getenv("BACKEND")
    API_TOKEN = os.getenv("API_TOKEN")
