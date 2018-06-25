from flask import Blueprint
from flask import current_app as app
from flask_restful import Api
from .editor import AssessEditor, TrainEditor
from ..backends.dummybackend import DummyBackend

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# TODO: Figure out how to load config before initialization/move this elsewhere
# api_url = app.config["API_URL"]
api_url = "/api/v1.0/"

# TODO: Turn this into config option
classifier = DummyBackend()

api.add_resource(AssessEditor,
                 api_url,
                 "/<string:editor_id>",
                 resource_class_kwargs={"classifier": classifier}
                 )

api.add_resource(TrainEditor,
                 api_url,
                 "/<string:editor_id>",
                 resource_class_kwargs={"classifier": classifier}
                 )
