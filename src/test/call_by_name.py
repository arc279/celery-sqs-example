from src.jobs.app import app, TASK_DEFAULT_QUEUE

# 外部から name 経由で呼ぶ

for x in range(32):
    ret = app.send_task(
        "sample_task_execute",
        kwargs={"something": "Hallo World"},
        queue=TASK_DEFAULT_QUEUE,
    )
    print(ret)
