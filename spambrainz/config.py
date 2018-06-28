import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "dev.db")
MB_DATABASE_URI = "postgres://localhost/users"

SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"

SECRET_KEY = "secret"

API_PREFIX = "/api/1.0"

BACKEND = "dummy"
