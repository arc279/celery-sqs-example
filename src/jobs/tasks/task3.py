import time
from celery import shared_task


@shared_task
def print_args(*args, **kwargs):
    time.sleep(3)
    print(locals())


@shared_task(name="calc_bmi")
def calc_bmi(weight: float, height: float) -> float:
    time.sleep(3)
    bmi = weight / height**2
    print(f"called calc_bmi {bmi}")
    return bmi


@shared_task(name="sample_task_execute")
def sample_task_execute(something: str):
    print(f"called sample_task_execute {something}")
    return something
