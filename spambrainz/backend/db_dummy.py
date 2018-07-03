from .base import Backend
from .utils import get_editor


class DbDummyBackend(Backend):
    def rate_editor(self, editor_id):
        if get_editor(editor_id):
            return True
        return False

    def train_editor(self, editor_id, is_spammer):
        if get_editor(editor_id):
            return True
        return False
