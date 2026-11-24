from typing import Annotated
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from util import load_projects, save_projects

app = FastAPI()
templates = Jinja2Templates(directory = "views")
projects = load_projects()

app.mount("/styles", StaticFiles(directory = "styles"), name = "styles")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request = request, name= "index.html", context = { "projects": projects[0:5] })

@app.get("/projects", response_class=HTMLResponse)
def get_projects(request: Request):
    return templates.TemplateResponse(request = request, name= "projects.html", context = { "projects": projects })

@app.get("/project/{id}", response_class=HTMLResponse)
def project_view(request: Request, id: int):
    return templates.TemplateResponse(request = request, name = "project.html", context = { "project": projects[id - 1]})

@app.post("/projects/new", response_class=RedirectResponse)
async def new_project(project_name: Annotated[str, Form()], project_description: Annotated[str, Form()]):
    global projects
    projects.append({"id": len(projects) + 1, "name": project_name, "description": project_description})
    save_projects(projects)
    return RedirectResponse("/projects", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/project/edit/{project_id}")
async def edit_project(project_id: int, project_name: Annotated[str, Form()], project_description: Annotated[str, Form()]):
    # TODO Implement me
    pass

@app.post("/project/delete/{project_id}")
async def delete_project(project_id: int):
    # TODO Implement me
    pass

if __name__ == "__main__":
    uvicorn.run("server:app")
