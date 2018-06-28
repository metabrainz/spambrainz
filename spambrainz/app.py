from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from .web.models import db
from .web.views import index
from .api.api import create_api_bp

toolbar = DebugToolbarExtension()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False, template_folder="web/templates")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db.init_app(app)

    if app.debug:
        toolbar.init_app(app)
        # reset_debug_db()

    backend_setting = app.config["BACKEND"]

    if backend_setting == "dummy":
        from .backends.dummy import DummyBackend
        backend = DummyBackend()
    else:
        mbdb_uri = app.config["MB_DATABASE_URI"]

        if backend_setting == "dbdummy":
            from .backends.db_dummy import DbDummyBackend
            backend = DbDummyBackend(db, mbdb_uri)
        else:
            from .backends.redis import redis, RedisBackend
            redis.init_app(app)
            backend = RedisBackend(db, mbdb_uri)

    app.register_blueprint(index.bp)
    app.register_blueprint(create_api_bp(backend), url_prefix=app.config["API_PREFIX"])

    return app
