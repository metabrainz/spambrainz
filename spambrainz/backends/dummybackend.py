from spambrainz.backends.classifier import Classifier


class DummyBackend(Classifier):
    def assess_editor(self, editor_id):
        return True

    def train_editor(self, editor_id, is_spammer):
        return True
