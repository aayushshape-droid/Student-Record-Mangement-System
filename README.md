# Student Record Management System

A menu-driven **Python console application** for managing student records
(ID, Name, Age, Course, Marks). All data is stored in memory during
execution and persisted to a local JSON file (`records.json`), so records
survive between program runs.

## Description

This application lets you add, view, search, update, and delete student
records through a simple numbered text menu. Every operation is written
as its own function with a docstring and inline comments, input is
validated in loops so the program never crashes on bad input, and every
add/update/delete immediately saves the full record set to
`records.json`.

## Features

- **Add Record** — enter ID, Name, Age, Course, and Marks for a new
  student; duplicate IDs are rejected automatically.
- **View All Records** — prints every record in a clean, aligned table.
- **Search Record** — search by exact Student ID or by a partial,
  case-insensitive Name match.
- **Update Record** — look up a student by ID and update any field,
  leaving a field blank to keep its current value.
- **Delete Record** — look up a student by ID and delete their record
  after a y/n confirmation prompt.
- **Persistent Storage** — records are loaded from `records.json` on
  startup and saved back to it after every add, update, or delete.
- **Robust Input Validation** — dedicated helper functions
  (`get_valid_integer`, `get_valid_float`, `get_non_empty_string`)
  re-prompt the user instead of crashing on invalid input.
- **Exception Handling** — `FileNotFoundError` and `json.JSONDecodeError`
  are handled when loading data, and file-write errors are caught when
  saving.

## Technologies Used

- **Python 3** — core programming language
- **JSON** — data storage format (`json` module)
- **File I/O** — reading/writing `records.json`
- **Functions** — one function per operation (`add_record`,
  `view_records`, `search_record`, `update_record`, `delete_record`,
  `save_to_file`, `load_from_file`, `display_menu`)
- **Exception Handling** — `try`/`except` blocks throughout for safe,
  crash-free execution

## Project Files

```
.
├── main.py         # The full application
├── records.json    # Sample/seed data (loaded automatically on startup)
└── README.md        # This file
```

## How to Run

1. Make sure you have **Python 3.6+** installed:
   ```bash
   python3 --version
   ```
2. Place `main.py` and `records.json` in the same folder.
3. Run the program from a terminal:
   ```bash
   python3 main.py
   ```
4. Use the on-screen menu (enter a number 1–6) to manage records. Data is
   saved to `records.json` automatically after every change, so you can
   close and reopen the program without losing data.

## Sample Input / Output

```
========================================
   STUDENT RECORD MANAGEMENT SYSTEM
========================================
1. Add Record
2. View All Records
3. Search Record (by ID or Name)
4. Update Record
5. Delete Record
6. Exit
========================================
Enter your choice (1-6): 2

--- All Student Records ---
ID      Name                Age   Course              Marks
------------------------------------------------------------
101     Alice Johnson       20    Computer Science    88.5
102     Bob Smith           22    Mathematics         75.0
103     Carla Mendes        21    Electrical Engineering91.2

Total records: 3

========================================
   STUDENT RECORD MANAGEMENT SYSTEM
========================================
1. Add Record
2. View All Records
3. Search Record (by ID or Name)
4. Update Record
5. Delete Record
6. Exit
========================================
Enter your choice (1-6): 1

--- Add New Student Record ---
Enter Student ID: 104
Enter Student Name: David Lee
Enter Student Age: 23
Enter Course: Physics
Enter Marks: 82.4
Record for 'David Lee' (ID: 104) added successfully.

========================================
   STUDENT RECORD MANAGEMENT SYSTEM
========================================
1. Add Record
2. View All Records
3. Search Record (by ID or Name)
4. Update Record
5. Delete Record
6. Exit
========================================
Enter your choice (1-6): 6
Exiting Student Record Management System. Goodbye!
```

### Example: invalid input handling

```
Enter your choice (1-6): abc
Invalid input. Please enter a whole number.
Enter your choice (1-6): 1

--- Add New Student Record ---
Enter Student ID: 101
Error: A record with ID 101 already exists. Please enter a different ID.
Enter Student ID: 105
...
```

## Notes

- `records.json` is created automatically the first time you add a
  record if it doesn't already exist.
- If `records.json` is missing or contains invalid JSON, the program
  logs a friendly warning and starts with an empty record list instead
  of crashing.
