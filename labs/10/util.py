from json import load, dump

def load_projects():
    try:
        with open("data/projects.json", "r") as f:
            return load(f)
    except FileNotFoundError:
        return []

def save_projects(projects):
    try:
        with open("data/projects.json", 'w') as f:
            dump(projects, f)
    except FileNotFoundError:
        return
