from os import environ
from celery import Celery
from celery.signals import worker_process_init
from sqlalchemy import create_engine

celery = Celery(
    "tasks",
    backend=environ["CELERY_RESULT_BACKEND"],
    broker=environ["CELERY_BROKER_URL"],
)

engine = None


@worker_process_init.connect()
def init_worker_process():
    global engine
    engine = create_engine(environ["MB_DATABASE_URI"])


@celery.task()
def write_report(score, editor_id):
    # Spamninja integration goes here
    pass
