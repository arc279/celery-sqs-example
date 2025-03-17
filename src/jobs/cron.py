from datetime import timedelta
from celery.schedules import crontab

from src.jobs.app import app


app.conf.beat_schedule = {
    "add_task": {
        "task": "src.jobs.worker.tasks.add",
        "schedule": timedelta(seconds=5),
        "args": (1, 2),
    },
    "print_message_task": {
        "task": "src.jobs.worker.tasks.print_message",
        "schedule": timedelta(seconds=7),
        "args": ("Hello, Celery!",),
        "kwargs": {"name": "Celery"},
    },
    "db_use_task": {
        "task": "src.jobs.worker.tasks.test_db",
        "schedule": timedelta(seconds=10),
    },
    "send-email-every-minute": {
        "task": "src.jobs.worker.tasks.send_email",
        "schedule": crontab(minute="*"),
        "args": ("example@example.com",),
    },
}
