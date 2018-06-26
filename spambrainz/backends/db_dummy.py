from spambrainz.backends.base import Backend


class DbDummyBackend(Backend):
    def __init__(self, db):
        self.db = db

    def rate_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
