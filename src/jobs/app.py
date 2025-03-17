# cf. https://qiita.com/hankehly/items/c3e0496eb04327a53ac4
import os
from celery import Celery

CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL"
    # "redis://localhost:6379/0",
)


app = Celery(__name__, broker=CELERY_BROKER_URL)
app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Tokyo",
    task_acks_late=True,  # タスクが完了してからAckする（タスクはべき等であるべき）
    task_reject_on_worker_lost=True,  # ワーカーの異常終了で、Ackされていないタスクを際スケジューリングする
)
