from collections import Counter
from datetime import date

def get_statistics(todos):
    total = len(todos)
    completed = sum(t.status == "Completed" for t in todos)
    pending = total - completed
    overdue = sum(
        t.status == "Pending" and t.due_date < date.today().isoformat()
        for t in todos
    )
    high_priority = sum(t.priority == "High" and t.status == "Pending" for t in todos)
    categories = Counter(t.category for t in todos)
    completion_rate = round((completed / total) * 100, 1) if total else 0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "high_priority": high_priority,
        "completion_rate": completion_rate,
        "categories": dict(categories)
    }