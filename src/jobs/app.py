# cf. https://qiita.com/hankehly/items/c3e0496eb04327a53ac4
import os
from celery import Celery

# 適切に IAM 権限が付与されていれば指定なしでも動作する
BROKER_URL = os.getenv("CELERY_BROKER_URL", "sqs://")
TASK_DEFAULT_QUEUE = os.getenv("CELERY_TASK_DEFAULT_QUEUE", "celery-sqs-example")

SQS_AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "ap-northeast-1")

app = Celery(__name__, broker=BROKER_URL)
print(f"queue name: {TASK_DEFAULT_QUEUE}")

# cf. https://qiita.com/hankehly/items/c3e0496eb04327a53ac4
app.conf.update(
    broker_transport_options={
        "region": SQS_AWS_REGION,
    },
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Tokyo",
    task_acks_late=True,  # タスクが完了してからAckする（タスクはべき等であるべき）
    task_reject_on_worker_lost=True,  # ワーカーの異常終了で、Ackされていないタスクを際スケジューリングする
    task_default_queue=TASK_DEFAULT_QUEUE,  # タスクが登録されるためのキュー名",
)
