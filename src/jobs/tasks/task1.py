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
