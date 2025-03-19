import time
from src.jobs.app import app, TASK_DEFAULT_QUEUE


@app.task(queue=TASK_DEFAULT_QUEUE)
def print_args(*args, **kwargs):
    time.sleep(3)
    print(locals())


@app.task(name="calc_bmi", queue=TASK_DEFAULT_QUEUE)
def calc_bmi(weight: float, height: float) -> float:
    time.sleep(3)
    bmi = weight / height**2
    print(f"called calc_bmi {bmi}")
    return bmi


@app.task(name="sample_task_execute", queue=TASK_DEFAULT_QUEUE)
def sample_task_execute(something: str):
    print(f"called sample_task_execute {something}")
    return something
