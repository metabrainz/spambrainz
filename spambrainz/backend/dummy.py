from spambrainz.backend.base import Backend


class DummyBackend(Backend):
    def rate_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
