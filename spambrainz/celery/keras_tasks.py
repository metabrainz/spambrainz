from os import environ
from celery import Celery
from celery.signals import worker_process_init

celery = Celery(
    "tasks",
    backend=environ["CELERY_RESULT_BACKEND"],
    broker=environ["CELERY_BROKER_URL"],
)

editor_model = None


@worker_process_init.connect()
def init_worker_process():
    global editor_model
    # import model
    pass


@celery.task()
def rate_editor(editor: dict):
    global editor_model
    # model.predict
    pass


@celery.task()
def train_editor(editor: dict):
    global editor_model
    # model.fit
    pass
