from spambrainz.backends.base import Backend


class DummyBackend(Backend):
    def assess_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
