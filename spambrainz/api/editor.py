from flask_restful import Resource, reqparse


class RateEditor(Resource):
    def __init__(self, **kwargs):
        self.backend = kwargs["backend"]

    def put(self, editor_id):
        if self.backend.rate_editor(editor_id):
            return {"status": "ok"}
        else:
            return {"status": "could not find editor"}


class TrainEditor(Resource):
    def __init__(self, **kwargs):
        self.backend = kwargs["backend"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("is_spammer", type=bool, required=True)

    def put(self, editor_id):
        args = self.parser.parse_args()

        if self.backend.train_editor(editor_id, args.is_spammer):
            return {"status": "ok"}
        else:
            return {"status": "could not find editor"}
