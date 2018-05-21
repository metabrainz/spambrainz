import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models.base import Base
from .models.user import User
from .views import index


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False, template_folder="templates")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("../config.py")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db = SQLAlchemy(app)

    # Recreate database in debug mode
    if app.debug:
        Base.metadata.drop_all(bind=db.engine)
        Base.metadata.create_all(bind=db.engine)
        db.session.add(User("admin", "adminPassword"))
        db.session.commit()

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(index.bp)

    return app
