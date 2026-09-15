from .models import Todo
from .storage import load_todos, save_todos

class TodoManager:
    def __init__(self):
        self.todos = load_todos()

    def next_id(self):
        return max((t.id for t in self.todos), default=0) + 1

    def add(self, title, description, due_date, priority, category):
        todo = Todo(self.next_id(), title.strip(), description.strip(),
                    due_date, priority, category.strip() or "General")
        self.todos.append(todo)
        save_todos(self.todos)
        return todo

    def update(self, todo_id, title, description, due_date, priority, category, status):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.title = title.strip()
                todo.description = description.strip()
                todo.due_date = due_date
                todo.priority = priority
                todo.category = category.strip() or "General"
                todo.status = status
                save_todos(self.todos)
                return True
        return False

    def delete(self, todo_id):
        old_count = len(self.todos)
        self.todos = [t for t in self.todos if t.id != todo_id]
        save_todos(self.todos)
        return len(self.todos) < old_count

    def complete(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                todo.status = "Completed"
                save_todos(self.todos)
                return True
        return False

    def all(self):
        return list(self.todos)

