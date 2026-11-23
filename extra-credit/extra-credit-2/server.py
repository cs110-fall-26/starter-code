from typing import Annotated
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory = "views")

notes = {}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context = { "notes": notes })

@app.post("/api/notes", response_class=RedirectResponse)
def new_note(name: Annotated[str, Form()], description: Annotated[str, Form()], tags: Annotated[str, Form()]):
    global notes
    notes[name] = { "name": name, "description": description, "tags": tags.split(",")}
    return RedirectResponse('/', status_code=status.HTTP_303_SEE_OTHER)

@app.post("/api/del_note", response_class=RedirectResponse)
def delete_note(name: Annotated[str, Form()]):
    global notes
    del notes[name]
    return RedirectResponse('/', status_code=status.HTTP_303_SEE_OTHER)

uvicorn.run("server:app")

