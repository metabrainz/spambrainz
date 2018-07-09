from flask_testing import TestCase
from spambrainz import app
from spambrainz.config import Config


class ApiTestCase(TestCase):
    def create_app(self):
        config = Config()
        config.BACKEND = "dummy"
        return app.create_app(config)

    def setUp(self):
        self.api_prefix = self.app.config["API_PREFIX"]

    def test_rate_editor(self):
        success = self.client.put(self.api_prefix + "/234/rate")
        failure = self.client.put(self.api_prefix + "/235/rate")

        self.assertEquals(success.json, dict(status="ok"))
        self.assertEquals(failure.json, dict(status="could not find editor"))

    def test_train_editor(self):
        error = self.client.put(self.api_prefix + "/234/train")
        success = self.client.put(self.api_prefix + "/234/train", data=dict(is_spammer=True))
        failure = self.client.put(self.api_prefix + "/235/train", data=dict(is_spammer=True))

        self.assertEquals(error.json, {"message": {"is_spammer": "Missing required parameter in the JSON body or the" +
                                                                 " post body or the query string"}})
        self.assertEquals(success.json, dict(status="ok"))
        self.assertEquals(failure.json, dict(status="could not find editor"))
