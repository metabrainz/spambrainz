from spambrainz.backends.base import Backend


class RedisBackend(Backend):
    def __init__(self, redis):
        self.redis = redis

    def assess_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
