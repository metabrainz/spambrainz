from flask_redis import FlaskRedis
from .db_backend import DbBackend

redis = FlaskRedis()


class RedisBackend(DbBackend):
    def rate_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
