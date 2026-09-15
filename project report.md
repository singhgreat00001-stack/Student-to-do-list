# Student To-Do List Manager — VITyarthi Project Report

## 1. Cover Page

**Project Title:** Student To-Do List Manager  
**Student Name:** __________________________  
**Registration Number:** ____________________  
**School/College:** _________________________  
**Course:** _________________________________  
**Academic Year:** 2026–27


## 2. Acknowledgement

I sincerely thank my teacher/mentor for guidance and support during the development of this project. I also thank my institution and classmates for providing the resources and encouragement required to complete the project.

## 3. Introduction

The Student To-Do List Manager is a Python-based desktop productivity application. It provides a centralized place for students to record tasks, deadlines, priorities and categories. The project demonstrates Python programming, modular design, file handling, validation, GUI development, searching, filtering, analytics, testing and Git version control.

## 4. Problem Statement

Students frequently have several assignments, projects, activities and deadlines. When tasks are recorded informally, important work can be missed. The proposed system organizes tasks in one application and shows their current status.

## 5. Objectives

- Create and manage personal tasks.
- Store task details permanently.
- Mark tasks as completed.
- Search and filter tasks.
- Identify overdue and high-priority tasks.
- Calculate completion statistics.
- Provide a simple graphical interface.
- Demonstrate modular software development.

## 6. Functional Requirements

### Module 1 — Task Management
Users can add, complete and delete tasks.

### Module 2 — Validation
The application checks that the title is present, the due date follows YYYY-MM-DD, and the priority is valid.

### Module 3 — Storage
Tasks are saved to a JSON file and loaded when the application starts.

### Module 4 — Search and Filtering
Users can search by title, description or category and filter by status or priority.

### Module 5 — Analytics
The system calculates total tasks, completed tasks, pending tasks, overdue tasks, high-priority pending tasks and completion rate.

### Module 6 — GUI
Tkinter provides the graphical user interface.

## 7.Non-Functional Requirements

1. **Usability:** Controls and labels are easy to understand.
2. **Reliability:** Data is validated before being saved.
3. **Maintainability:** Code is separated into logical modules.
4. **Performance:** Local JSON operations are fast for normal personal use.
5. **Portability:** The application can run on systems with Python and Tkinter.
6. **Error Handling:** Invalid input displays a user-friendly error.
7. **Resource Efficiency:** No external database server is required.
8. **Scalability:** The architecture allows future modules such as reminders and cloud storage.

## 8. System Architecture

The application uses a layered architecture:
- GUI layer
- Task-management layer
- Validation/search/analytics services
- Storage layer
- JSON data file

See `docs/architecture.txt`.

## 9. Design Diagrams

The repository contains descriptions for:
- System architecture
- Workflow
- Use-case diagram
- Sequence diagram
- Class diagram
- Data/ER design

For final submission, these descriptions can be recreated as graphical diagrams in draw.io, Word or PowerPoint.

## 10. Implementation

### Data Model
The `Todo` class stores ID, title, description, due date, priority, category and status.

### Task Manager
`TodoManager` implements task creation, updating, deletion, completion and retrieval.

### Validation
`validators.py` checks required information and date/priority validity.

### Storage
`storage.py` reads and writes JSON data.

### Search
`search.py` performs keyword and filter operations.

### Analytics
`analytics.py` generates task statistics.

### User Interface
`ui.py` provides the Tkinter desktop interface.

## 11. Testing

The project includes unit tests for:
- Valid and invalid task input
- Search functionality
- Status filtering
- Task statistics

Run:

```bash
pytest
```

Example test cases:

| Test | Expected Result |
|---|---|
| Empty title | Rejected |
| Invalid date | Rejected |
| Valid task | Accepted |
| Search "Python" | Matching task displayed |
| Completed filter | Only completed tasks displayed |
| Statistics | Correct totals calculated |

## 12. Screenshots / Results

After running the application, capture screenshots of:
1. Main To-Do List window.
2. Adding a new task.
3. Validation error.
4. Search/filter results.
5. Completed task.
6. Statistics displayed at the bottom.

## 13. Challenges and Solutions

**Challenge:** Keeping tasks after restarting the application.  
**Solution:** Implemented JSON-based persistent storage.

**Challenge:** Preventing invalid dates.  
**Solution:** Added date validation.

**Challenge:** Finding relevant tasks quickly.  
**Solution:** Added keyword search and status/priority filters.

**Challenge:** Keeping code manageable.  
**Solution:** Divided the application into separate modules.

## 14. Learning Outcomes

This project provided practical understanding of:
- Python classes and objects
- Functions and modules
- File handling
- JSON
- GUI programming
- Input validation
- Searching and filtering
- Basic analytics
- Unit testing
- Git and GitHub
- Software architecture and documentation

## 15.. Future Enhancements

- Edit tasks directly from the GUI.
- Add calendar-based task view.
- Add reminder notifications.
- Export tasks to CSV/PDF.
- Add user accounts.
- Add cloud database synchronization.
- Add dark mode.
- Add recurring tasks.

## 16. Conclusion

The Student To-Do List Manager provides a practical solution for organizing daily tasks and deadlines. It satisfies the main requirements of a modular software project while remaining easy to understand and demonstrate. The project can also be extended with advanced features such as reminders, cloud synchronization and multi-user collaboration.

## 17.. References

- Python documentation
- Tkinter documentation
- Git documentation
- GitHub documentation
- VITyarthi Build Your Own Project guidelines
