# CLI Task Manager 📝

A simple and interactive Python CLI-based Task Manager to help you stay organized. Add, delete, and toggle tasks directly from your terminal, with data saved persistently in JSON format.

---

## Features

- **Add Tasks**: Create new tasks with a timestamp.
- **Delete Tasks**: Remove tasks by their ID.
- **Toggle Task Status**: Mark tasks as complete (`✅`) or incomplete (`❌`).
- **Persistent Storage**: Tasks are saved in a JSON file and reloaded when you restart the program.
- **Error Handling**: Handles invalid inputs and corrupted files gracefully.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cli-task-manager.git
   cd cli-task-manager

2. **Run the program**
	```bash
	python main.py

3. **Commands**
	A: Add a new task.
	D: Delete an existing task by its ID.
	C: Toggle the completion status of a task.
	Q: Quit the program (tasks are saved automatically).

## Example output

+----+----------------------------------------+--------------------+--------------------+
| ID |              Title                     |     created at     |       status       |
+----+----------------------------------------+--------------------+--------------------+
|  1 | Buy groceries                          |    12/19, 10:30    |         ✅         |
|  2 | Finish Python Piscine exercise         |    12/19, 12:00    |         ❌         |
+----+----------------------------------------+--------------------+--------------------+
(A)dd, (D)el, (C)hange status, (Q)uit:
