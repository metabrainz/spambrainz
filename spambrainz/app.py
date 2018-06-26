from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_redis import FlaskRedis
from .web.models import db
from .web.views import index
from .api.api import create_api_bp
from .backends.dummy import DummyBackend

toolbar = DebugToolbarExtension()
redis = FlaskRedis()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False, template_folder="web/templates")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    redis.init_app(app)
    db.init_app(app)

    if app.debug:
        toolbar.init_app(app)
        # reset_debug_db()

    backend = DummyBackend()

    app.register_blueprint(index.bp)
    app.register_blueprint(create_api_bp(backend), url_prefix=app.config["API_PREFIX"])

    return app
