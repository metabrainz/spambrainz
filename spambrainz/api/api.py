from flask import Blueprint
from flask_restful import Api
from werkzeug.urls import url_join
from .editor import RateEditor, TrainEditor
from ..backends.dummy import DummyBackend


def create_api_bp():
    api_bp = Blueprint("api", __name__)
    api = Api(api_bp)

    # TODO: Turn this into config option
    backend = DummyBackend()

    api.add_resource(RateEditor,
                     "/<string:editor_id>/rate",
                     resource_class_kwargs={"backend": backend}
                     )

    api.add_resource(TrainEditor,
                     "/<string:editor_id>/train",
                     resource_class_kwargs={"backend": backend}
                     )

    return api_bp
