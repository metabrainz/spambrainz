from .db_backend import DbBackend


class DbDummyBackend(DbBackend):
    def rate_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
