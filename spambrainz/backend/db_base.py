from spambrainz.backend.base import Backend
from brainzutils.musicbrainz_db import init_db_engine
from brainzutils.musicbrainz_db.editor import get_editor_by_id
import brainzutils.musicbrainz_db.exceptions as mb_exceptions


class DbBackend(Backend):
    def __init__(self, conn_str):
        # Initialize brainzutils DB engine
        init_db_engine(conn_str)

    def get_editor(self, editor_id):
        try:
            return get_editor_by_id(editor_id)
        except mb_exceptions.NoDataFoundException:
            return None

    def write_report(self, editor_id, score):
        pass
