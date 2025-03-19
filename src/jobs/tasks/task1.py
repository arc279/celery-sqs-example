import time
from sqlalchemy import text

from src.jobs import db
from src.jobs.app import app, TASK_DEFAULT_QUEUE


@app.task(queue=TASK_DEFAULT_QUEUE)
def hello():
    time.sleep(3)
    print("hello")


@app.task(queue=TASK_DEFAULT_QUEUE)
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
