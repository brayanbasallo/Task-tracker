import typer
import json
from datetime import datetime
app = typer.Typer()

def get_json():
    with open("data.json", "r") as f:
        return json.load(f)

@app.command()
def add(task: str):
    json_data = get_json()
    task_id = len(json_data["tasks"]) + 1
    json_data["tasks"][task_id] = {}
    json_data["tasks"][task_id]["task"] = task
    json_data["tasks"][task_id]["completed"] = False
    json_data["tasks"][task_id]["created_at"] = datetime.now().isoformat()
    json_data["tasks"][task_id]["updated_at"] = datetime.now().isoformat()
    json_data["tasks"][task_id]["completed_at"] = None
    json_data["tasks"][task_id]["in_progress"] = False
    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Added task: {task_id}: {task}")

@app.command()
def list(status: str = None):
    json_data = get_json()
    if not json_data["tasks"]:
        print("No tasks found")
        return
    if status:
        for task_id, task in json_data["tasks"].items():
            if task["in_progress"] and status == "in-progress":
                print(f"{task_id}: {task['task']}")
            elif task["completed"] and status == "completed":
                print(f"{task_id}: {task['task']}")
            elif not task["in_progress"] and not task["completed"] and status == "todo":
                print(f"{task_id}: {task['task']}")
    else:
        for task_id, task in json_data["tasks"].items():
            print(f"{task_id}: {task['task']}")
        
@app.command()
def delete(task_id: str):
    json_data = get_json()
    if task_id not in json_data["tasks"]:
        print(f"Task with ID {task_id} not found")
        return
    del json_data["tasks"][task_id]
    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Deleted task with ID {task_id}")
    
@app.command()
def update(task_id: str, task: str):
    json_data = get_json()
    if task_id not in json_data["tasks"]:
        print(f"Task with ID {task_id} not found")
        return
    json_data["tasks"][task_id]["task"] = task
    json_data["tasks"][task_id]["updated_at"] = datetime.now().isoformat()

    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Updated task with ID {task_id}")

@app.command()
def in_progress(task_id: str, in_progress: bool):
    json_data = get_json()
    if task_id not in json_data["tasks"]:
        print(f"Task with ID {task_id} not found")
        return
    json_data["tasks"][task_id]["in_progress"] = in_progress
    json_data["tasks"][task_id]["updated_at"] = datetime.now().isoformat()

    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Updated task with ID {task_id}")
    
@app.command()
def complete(task_id: str, completed: bool):
    json_data = get_json()
    if task_id not in json_data["tasks"]:
        print(f"Task with ID {task_id} not found")
        return
    json_data["tasks"][task_id]["completed"] = completed
    json_data["tasks"][task_id]["completed_at"] = datetime.now().isoformat()
    json_data["tasks"][task_id]["updated_at"] = datetime.now().isoformat()

    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Updated task with ID {task_id}")    
    
@app.command()
def delete_all():
    json_data = get_json()
    json_data["tasks"] = {}
    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print("Deleted all tasks")

if __name__ == "__main__":
    app()