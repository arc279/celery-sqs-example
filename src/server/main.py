from typing import Optional, Any
from fastapi import FastAPI
from pydantic import BaseModel

from src.jobs.tasks import task1, task2, task3
from src.jobs.app import TASK_DEFAULT_QUEUE

app = FastAPI()


class Body(BaseModel):
    weight: float
    height: float


class TaskRequest(BaseModel):
    id: str


@app.get("/hello")
def hello():
    print("call hello delay")
    task1.hello.delay()
    # task1.hello.apply_async(queue=TASK_DEFAULT_QUEUE)
    return "OK"


@app.get("/hello2")
def hello2():
    print("call hello now")
    task1.hello()
    return "OK"


@app.get("/db")
def test_db():
    print("call db delay")
    task1.test_db.apply_async()
    return "OK"


@app.post("/bmi", response_model=TaskRequest, response_model_exclude_unset=True)
def calculate_bmi(body: Body):
    task = task3.calc_bmi.apply_async(
        kwargs=dict(weight=body.weight, height=body.height),
    )
    print(task, type(task))
    return TaskRequest(id=task.id)
