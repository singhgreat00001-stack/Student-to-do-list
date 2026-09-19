# Student To-Do List Manager

A modular Python desktop To-Do List application designed for student task and assignment management, developed for the VITyarthi Project submission.

## Features

- Create tasks with title, description, due date, priority, and category
- Mark tasks as completed
- Delete tasks with confirmation
- Real-time search across tasks
- Filter by status (All, Pending, Completed) and priority (Low, Medium, High)
- Overdue task detection
- Dynamic completion-rate analytics
- High-priority task counting
- Tkinter graphical user interface
- Automated unit test suite
- Modular architecture separating UI, business logic, storage, and models

## Technology Stack

- **Python 3.10+**
- **Tkinter** (Standard Library GUI)
- **Dataclasses & JSON** (Built-in serialization)
- **Pytest** (Automated unit testing)
- **Git & GitHub** (Version control)

## Project Structure

```text
Student-to-do-list/
├── main.py                     # Application entry point
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
├── statement.md                # Problem statement and scope
├── Project report.pdf          # Formatted academic project report
├── data/
│   └── todos.json              # Local JSON task storage
├── docs/                       # Design and architecture diagrams
│   ├── architecture.txt
│   ├── class_diagram.txt
│   ├── er_diagram.txt
│   ├── sequence.txt
│   ├── use_case.txt
│   └── workflow.txt
├── Screenshots/                # Application execution captures
│   ├── 1_main_interface.png
│   ├── 2_add_task_form.png
│   ├── 3_search_filter.png
│   ├── 4_priority_filter.png
│   └── 5_completed_task.png
└── todo_app/                   # Application source package
    ├── __init__.py
    ├── analytics.py            # Statistics and completion rate logic
    ├── models.py               # Todo data model
    ├── search.py               # Search and filtering algorithms
    ├── storage.py              # JSON read/write persistence
    ├── task_manager.py         # CRUD manager logic
    ├── ui.py                   # Tkinter desktop interface
    ├── validators.py           # Input and date validation
    └── tests/
        └── test_todo.py        # Pytest unit tests
```

## How to Run

1. Ensure Python 3.10 or newer is installed:
   ```bash
   python --version
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Running Unit Tests

Install pytest if not already installed:
```bash
pip install -r requirements.txt
```

Execute the test suite:
```bash
pytest todo_app/tests
```

## Repository Management

```bash
git add .
git commit -m "Update project structure and report"
git push origin main
```

## Future Improvements

- In-place task editing from the GUI
- Calendar schedule view
- System tray reminder notifications
- CSV and PDF task export
- Multi-user authentication
- Cloud database synchronization
