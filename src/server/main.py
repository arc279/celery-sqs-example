from typing import Optional, Any
from fastapi import FastAPI
from pydantic import BaseModel

from src.worker import tasks

app = FastAPI()


class Body(BaseModel):
    weight: float
    height: float


class TaskRequest(BaseModel):
    id: str


@app.get("/hello")
def hello():
    print("call hello delay")
    tasks.hello.delay()


@app.get("/hello2")
def hello2():
    print("call hello now")
    tasks.hello()


@app.post("/bmi", response_model=TaskRequest, response_model_exclude_unset=True)
def calculate_bmi(body: Body):
    task = tasks.calc_bmi.delay(weight=body.weight, height=body.height)
    print(task, type(task))
    return TaskRequest(id=task.id)
