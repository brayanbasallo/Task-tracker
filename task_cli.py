import typer
import json

app = typer.Typer()

def get_json():
    with open("data.json", "r") as f:
        return json.load(f)

@app.command()
def add(task: str):
    json_data = get_json()
    task_id = len(json_data["tasks"]) + 1
    json_data["tasks"][task_id] = task
    with open("data.json", "w") as f:
        json.dump(json_data, f)
    print(f"Added task: {task_id}: {task}")

@app.command()
def list():
    json_data = get_json()
    if not json_data["tasks"]:
        print("No tasks found")
        return

    for task_id, task in json_data["tasks"].items():
        print(f"{task_id}: {task}")
        
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
if __name__ == "__main__":
    app()