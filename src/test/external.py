from src.jobs.app import app

# 外部から name 経由で呼ぶ

for x in range(64):
    ret = app.send_task("sample_task_execute", kwargs={"something": "Hallo World"})
    print(ret)
