from flask_testing import TestCase
from spambrainz import app
from spambrainz.config import Config


class ApiTestCase(TestCase):
    def create_app(self):
        config = Config()
        config.BACKEND = "dummy"
        config.API_TOKEN = "test_token"
        return app.create_app(config)

    def setUp(self):
        self.api_prefix = self.app.config["API_PREFIX"]

    def test_token(self):
        notoken_message = {"message": {"token": "Missing required parameter in the JSON body or the" +
                                                " post body or the query string"}}

        notoken_rate = self.client.put(self.api_prefix + "/234/rate")
        notoken_train = self.client.put(self.api_prefix + "/234/train", data=dict(is_spammer=True))

        self.assertEqual(notoken_rate.json, notoken_message)
        self.assertEqual(notoken_train.json, notoken_message)

        wrongtoken_rate = self.client.put(self.api_prefix + "/234/rate", data=dict(token="abc"))
        wrongtoken_train = self.client.put(self.api_prefix + "/234/train", data=dict(is_spammer=True, token="abc"))

        self.assert403(wrongtoken_rate)
        self.assert403(wrongtoken_train)

    def test_rate_editor(self):
        success = self.client.put(self.api_prefix + "/234/rate", data=dict(token="test_token"))
        failure = self.client.put(self.api_prefix + "/235/rate", data=dict(token="test_token"))

        self.assertEquals(success.json, dict(status="ok"))
        self.assertEquals(failure.json, dict(status="could not find editor"))

    def test_train_editor(self):
        error = self.client.put(self.api_prefix + "/234/train", data=dict(token="test_token"))
        success = self.client.put(self.api_prefix + "/234/train", data=dict(is_spammer=True, token="test_token"))
        failure = self.client.put(self.api_prefix + "/235/train", data=dict(is_spammer=True, token="test_token"))

        self.assertEquals(error.json, {"message": {"is_spammer": "Missing required parameter in the JSON body or the" +
                                                                 " post body or the query string"}})
        self.assertEquals(success.json, dict(status="ok"))
        self.assertEquals(failure.json, dict(status="could not find editor"))
