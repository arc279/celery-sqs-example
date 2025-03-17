from src.jobs.worker import tasks

# 外部から直接タスクを呼ぶ

for x in range(64):
    # result = add.delay(x, x)
    result = tasks.add.apply_async((x, x))
    print(result)
