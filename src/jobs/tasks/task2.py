import time
from src.jobs.app import app, TASK_DEFAULT_QUEUE


@app.task(queue=TASK_DEFAULT_QUEUE)
def add(x, y):
    time.sleep(3)
    ret = x + y
    print(f"called add {x} {y} {ret}")
    return ret


@app.task(queue=TASK_DEFAULT_QUEUE)
def send_email(email: str):
    time.sleep(5)
    print(locals())
