from typing import Annotated
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from util import load_tasks, save_tasks

app = FastAPI()
templates = Jinja2Templates(directory = "views")

name = "User" # TODO Replace with your name

tasks = load_tasks()

class Task(BaseModel):
    task: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # TODO Implement me together

@app.post("/api/send", response_class=RedirectResponse)
async def send(task: Annotated[str, Form()]):
    # TODO Implement me together

uvicorn.run("server:app")
