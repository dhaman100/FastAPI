from fastapi import FastAPI
from pydantic import BaseModel
from  typing import List, Optional
from uuid import UUID,uuid4

app=FastAPI()

class Task(BaseModel):
    id :Optional[UUID] =None
    title :str
    description: Optional[str] = None
    Completed: bool =False

tasks =[]

@app.post("/tasks",response_model=Task)
def create_task(task: Task):
    task.id =uuid4()
    tasks.append(task)
    return task

@app.get("/task/",response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/")
def read_root():
    return { "name":"Dhaman","Age":24,"address":["A","B","C"]}