def filter_todos(todos, keyword="", status="All", priority="All"):
    keyword = keyword.strip().lower()
    result = []

    for todo in todos:
        matches_keyword = (
            not keyword
            or keyword in todo.title.lower()
            or keyword in todo.description.lower()
            or keyword in todo.category.lower()
        )
        matches_status = status == "All" or todo.status == status
        matches_priority = priority == "All" or todo.priority == priority

        if matches_keyword and matches_status and matches_priority:
            result.append(todo)

    return result