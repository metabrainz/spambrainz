from .db_base import DbBackend


class DbDummyBackend(DbBackend):
    def rate_editor(self, editor_id):
        if self.get_editor(editor_id):
            return True
        return False

    def train_editor(self, editor_id, is_spammer):
        if self.get_editor(editor_id):
            return True
        return False
