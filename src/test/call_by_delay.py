from src.jobs.tasks import task2
from src.jobs.app import TASK_DEFAULT_QUEUE


# 外部から直接タスクを呼ぶ

for x in range(32):
    # result = add.delay(x, x)
    result = task2.add.apply_async((x, x), queue=TASK_DEFAULT_QUEUE)
    # print(result)
