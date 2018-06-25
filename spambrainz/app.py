import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .web.models.base import Base
from .web.models.user import User
from .web.views import index
from .api.api import api_bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False, template_folder="web/templates")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db = SQLAlchemy(app)

    # Recreate database in debug mode
    if app.debug:
        Base.metadata.drop_all(bind=db.engine)
        Base.metadata.create_all(bind=db.engine)
        db.session.add(User("admin", "adminPassword"))
        db.session.commit()

    app.register_blueprint(index.bp)
    app.register_blueprint(api_bp)

    return app
