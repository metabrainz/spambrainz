from celery import Celery
from celery.signals import worker_process_init
from .config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

celery = Celery(
    "tasks",
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL
)

editor_model = None


@worker_process_init.connect()
def init_worker_process():
    global editor_model
    # keras imports
    pass


@celery.task()
def rate_editor(editor):
    global editor_model
    pass


@celery.task()
def train_editor(editor):
    global editor_model
    pass


@celery.task()
def write_report(score, editor_id):
    pass
