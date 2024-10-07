# Task CLI - CLI application for managing tasks 
Practical project for the "Task Tracker" project in the [roadmap.sh](https://roadmap.sh/projects/task-tracker).

A command-line interface (CLI) application for managing tasks, built with Python and Typer.

This application allows you to add, list, delete, update, mark tasks as in progress or completed, and delete all tasks.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the CLI application using:


Available commands:

- `add`: Add a new task
- `list`: List all tasks (optional status filter)
- `delete`: Delete a task
- `update`: Update a task
- `in_progress`: Mark a task as in progress
- `complete`: Mark a task as completed
- `delete_all`: Delete all tasks

For detailed usage of each command, use:
```
python task_cli.py <command> --help
```

## Examples

1. Add a task:
   ```
   python task_cli.py add "Buy groceries"
   ```

2. List all tasks:
   ```
   python task_cli.py list
   ```

3. List tasks by status:
   ```
   python task_cli.py list --status todo
   ```

4. Update a task:
   ```
   python task_cli.py update 1 "Buy organic groceries"
   ```

5. Mark a task as completed:
   ```
   python task_cli.py complete 1 true
   ```

## Project Structure

- `task_cli.py`: Main CLI application
- `src/app.py`: Example Typer application (not used in main CLI)
- `requirements.txt`: Project dependencies
- `data.json`: JSON file for storing task data
