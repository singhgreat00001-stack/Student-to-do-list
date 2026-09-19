# Student-to-do-list
tells about a proper description of an ideal student to do list. Student to do list is a simple and user friendly programme that helps student organize their daily tasks,assignment and all other tasks
# Student To-Do List Manager

A complete Python desktop To-Do List project designed for a VITyarthi-style Build Your Own Project submission.

## Features

- Create tasks with title, description, due date, priority and category
- Mark tasks as completed
- Delete tasks
- Search tasks
- Filter by status and priority
- Overdue-task detection
- Completion-rate analytics
- High-priority task count
- Tkinter graphical user interface
- Unit tests
- Modular architecture

## Technology Stack

- Python 3
- Tkinter
  
- Dataclasses
- Pytest for optional tests
- Git and GitHub

## Project Structure

```text
Student_Todo_List_VITyarthi/
├── main.py
├── README.md
├── statement.md
├── PROJECT_REPORT.pdf
├── requirements.txt
├── todo_app/
│   ├── models.py
│   ├── storage.py
│   ├── validators.py
│   ├── task_manager.py
│   ├── analytics.py
│   ├── search.py
│   └── ui.py
├── tests/
│   └── test_todo.py
└── docs/
    ├── architecture.txt
    ├── workflow.txt
    ├── use_case.txt
    ├── sequence.txt
    ├── class_diagram.txt
    └── er_diagram.txt
```

## How to Run

Install Python 3.10 or newer.

```bash
python main.py
```

## Testing

Install pytest if needed:

```bash
pip install pytest
```

Then:

```bash
pytest
```

## GitHub Upload

```bash
git init
git add .
git commit -m "Create Student To-Do List Manager"
git branch -M main
git remote add origin https://github.com/singhgreat00001-stack/Student-to-do-list.git
git push -u origin main
```


## Future Improvements

- Edit task from the GUI
- Calendar view
- Reminder notifications
- CSV/PDF export
- User login
- Cloud synchronization

