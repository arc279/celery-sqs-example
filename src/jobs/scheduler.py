from datetime import timedelta
from celery.schedules import crontab

from src.jobs.app import app


app.conf.beat_schedule = {
    "add_task": {
        "task": "src.jobs.tasks.task2.add",
        "schedule": timedelta(seconds=5),
        "args": (1, 2),
    },
    "print_args_task": {
        "task": "src.jobs.tasks.task3.print_args",
        "schedule": timedelta(seconds=7),
        "args": ("Hello, Celery!",),
        "kwargs": {"name": "Celery"},
    },
    "db_use_task": {
        "task": "src.jobs.tasks.task1.test_db",
        "schedule": timedelta(seconds=10),
    },
    "send-email-every-minute": {
        "task": "src.jobs.tasks.task2.send_email",
        "schedule": crontab(minute="*"),
        "args": ("example@example.com",),
    },
    "sample_task_execute": {
        "task": "sample_task_execute",
        "schedule": timedelta(seconds=3),
        "kwargs": {"something": "else"},
    },
}
