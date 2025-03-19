import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

import os

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import scoped_session, sessionmaker

uri = os.environ.get(
    "MYSQL_URI"
    # , "mysql+mysqlconnector://root:@127.0.0.1:3306/world"
)
print(f"mysql: {uri}")
engine = create_engine(uri)  # type: ignore


session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


if __name__ == "__main__":
    with session.begin():
        sql = """
        select
        *
        from world.city
        """
        row = session.execute(text(sql))
        print(len(row.fetchall()))
