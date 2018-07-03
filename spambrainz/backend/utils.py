from brainzutils.musicbrainz_db.editor import get_editor_by_id
import brainzutils.musicbrainz_db.exceptions as mb_exceptions


def get_editor(editor_id):
    """Return editor serialized to dict, None if not found."""
    try:
        return get_editor_by_id(editor_id)
    except mb_exceptions.NoDataFoundException:
        return None
