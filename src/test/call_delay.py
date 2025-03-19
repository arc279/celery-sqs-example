from src.jobs.tasks import task2

# 外部から直接タスクを呼ぶ

for x in range(64):
    # result = add.delay(x, x)
    result = task2.add.apply_async((x, x))
    print(result)
