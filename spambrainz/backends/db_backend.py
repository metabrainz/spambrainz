from spambrainz.backends.base import Backend
from brainzutils.musicbrainz_db import init_db_engine
from brainzutils.musicbrainz_db.editor import get_editor_by_id


class DbBackend(Backend):
    def __init__(self, conn_str):
        # Initialize brainzutils DB engine
        init_db_engine(conn_str)

    def rate_editor(self, editor_id):
        pass

    def train_editor(self, editor_id, is_spammer):
        pass

    def get_editor(self, id):
        return get_editor_by_id(id)
