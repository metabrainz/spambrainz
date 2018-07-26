from .base import Backend
from .utils import get_editor
from spambrainz.celery import keras_tasks, report_tasks


class CeleryBackend(Backend):
    def rate_editor(self, editor_id: int) -> bool:
        editor = get_editor(editor_id)
        if editor:
            # TODO: Connection error handling
            keras_tasks.rate_editor.apply_async(editor, link=report_tasks.write_report(editor_id))
            return True
        else:
            return False

    def train_editor(self, editor_id: int, is_spammer: bool) -> bool:
        editor = get_editor(editor_id)
        if editor:
            keras_tasks.train_editor.apply_async(editor)
            return True
        else:
            return False
