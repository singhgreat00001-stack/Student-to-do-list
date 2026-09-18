from todo_app.models import Todo
from todo_app.validators import validate_todo
from todo_app.search import filter_todos
from todo_app.analytics import get_statistics

def sample_tasks():
    return [
        Todo(1, "Finish Python", "Loops assignment", "2099-01-01", "High", "Study", "Pending"),
        Todo(2, "Read book", "Chapter 3", "2099-01-02", "Low", "Personal", "Completed"),
        Todo(3, "Project report", "Write introduction", "2099-01-03", "Medium", "Project", "Pending")
    ]

def test_validation():
    assert validate_todo("Task", "2099-01-01", "High")[0]
    assert not validate_todo("", "2099-01-01", "High")[0]
    assert not validate_todo("Task", "wrong-date", "High")[0]

def test_search():
    results = filter_todos(sample_tasks(), keyword="python")
    assert len(results) == 1

def test_filters():
    results = filter_todos(sample_tasks(), status="Completed")
    assert len(results) == 1

def test_statistics():
    stats = get_statistics(sample_tasks())
    assert stats["total"] == 3
    assert stats["completed"] == 1
    assert stats["pending"] == 2
