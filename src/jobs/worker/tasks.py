import time
from sqlalchemy import text

from src.jobs.app import app
from src.jobs import db


@app.task
def test_db():
    print("called hello")
    with db.session.begin():
        sql = """
        select
          *
        from world.city
        limit 10
        """
        row = db.session.execute(text(sql))
        print(row.fetchall())


@app.task
def add(x, y):
    time.sleep(3)
    ret = x + y
    print(f"called add {x} {y} {ret}")
    return ret


@app.task
def print_message(*args, **kwargs):
    time.sleep(3)
    print(locals())


@app.task
def send_email(email: str):
    time.sleep(5)
    print(locals())


@app.task()
def calc_bmi(weight: float, height: float) -> float:
    time.sleep(3)
    bmi = weight / height**2
    print(f"called calc_bmi {bmi}")
    return bmi


@app.task(name="sample_task_execute")
def sample_task_execute(something: str):
    print(f"called sample_task_execute {something}")
    return something
