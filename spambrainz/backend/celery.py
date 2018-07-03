from .base import Backend
from .utils import get_editor
from .. import celery_tasks


class CeleryBackend(Backend):
    def rate_editor(self, editor_id):
        editor = get_editor(editor_id)
        if editor:
            # TODO: Connection error handling
            celery_tasks.rate_editor.apply_async(editor, link=celery_tasks.write_report(editor_id))
            return True
        else:
            return False

    def train_editor(self, editor_id, is_spammer):
        editor = get_editor(editor_id)
        if editor:
            celery_tasks.train_editor.apply_async(editor)
            return True
        else:
            return False
