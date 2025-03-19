import time
from celery import shared_task


@shared_task
def add(x, y):
    time.sleep(3)
    ret = x + y
    print(f"called add {x} {y} {ret}")
    return ret


@shared_task
def send_email(email: str):
    time.sleep(5)
    print(locals())
