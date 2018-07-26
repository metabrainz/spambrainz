from spambrainz.backend.base import Backend


class DummyBackend(Backend):
    def rate_editor(self, editor_id: int) -> bool:
        if int(editor_id) % 2 == 0:
            return True
        else:
            return False

    def train_editor(self, editor_id: int, is_spammer: bool) -> bool:
        if int(editor_id) % 2 == 0:
            return True
        else:
            return False
