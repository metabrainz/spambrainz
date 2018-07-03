from .db_base import DbBackend
from .. import celery_tasks


class CeleryBackend(DbBackend):
    def rate_editor(self, editor_id):
        editor = self.get_editor(editor_id)
        if editor:
            result = celery_tasks.rate_editor(editor)
            return True
        else:
            return False

    def train_editor(self, editor_id, is_spammer):
        editor = self.get_editor(editor_id)
        if editor:
            result = celery_tasks.train_editor(editor)
            return True
        else:
            return False
