from flask import Blueprint
from flask_restful import Api
from .editor import RateEditor, TrainEditor
from ..backend.base import Backend


def create_api_bp(backend: Backend, token: str) -> Blueprint:
    api_bp = Blueprint("api", __name__)
    api = Api(api_bp)

    api.add_resource(RateEditor,
                     "/<string:editor_id>/rate",
                     resource_class_kwargs={"backend": backend, "token": token}
                     )

    api.add_resource(TrainEditor,
                     "/<string:editor_id>/train",
                     resource_class_kwargs={"backend": backend, "token": token}
                     )

    return api_bp
