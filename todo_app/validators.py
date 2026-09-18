from datetime import datetime

PRIORITIES = {"Low", "Medium", "High"}
STATUSES = {"Pending", "Completed"}

def validate_todo(title, due_date, priority):
    if not title.strip():
        return False, "Task title is required."
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return False, "Due date must use YYYY-MM-DD format."
    if priority not in PRIORITIES:
        return False, "Please select a valid priority."
    return True, ""

def validate_status(status):
    return status in STATUSES