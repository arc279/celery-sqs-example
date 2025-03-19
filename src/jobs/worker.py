# cf. https://ravinder-chadha.medium.com/multi-process-different-tasks-with-the-same-worker-in-python-using-celery-cee303decf27
from src.jobs.tasks.task1 import *
from src.jobs.tasks.task2 import *
from src.jobs.tasks.task3 import *

# これがないと動かないので注意
from src.jobs.app import app
