import json
from pathlib import Path
from .models import Todo

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "todos.json"

def load_todos():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [Todo.from_dict(x) for x in json.load(f)]
    except (OSError, json.JSONDecodeError):
        return []

def save_todos(todos):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([todo.to_dict() for todo in todos], f, indent=2)


