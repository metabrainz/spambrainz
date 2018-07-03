from spambrainz.backend.base import Backend


class DummyBackend(Backend):
    def rate_editor(self, editor_id):
        if int(editor_id) % 2 == 0:
            return True
        else:
            return False

    def train_editor(self, editor_id, is_spammer):
        if int(editor_id) % 2 == 0:
            return True
        else:
            return False
