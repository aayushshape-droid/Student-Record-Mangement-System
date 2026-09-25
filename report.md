# Assignment Report

**Student Name:** Aayush Shape
**Date:** 26 September 2026
**Subject:** Programming of Python & Relational Databases
**Project Title:** Student Record Management System

---

## 1. Introduction

Educational institutions handle large volumes of student information such
as ID numbers, names, ages, enrolled courses, and academic marks.
Maintaining this data manually on paper or in scattered files is slow,
error-prone, and difficult to search or update. The **Student Record
Management System** is a menu-driven console application built in Python
that solves this problem by providing a simple, reliable way to add,
view, search, update, and delete student records, while automatically
saving all data to a JSON file so that it is never lost between program
runs.

This project was developed as part of the *Programming of Python &
Relational Databases* course to demonstrate practical understanding of
core Python programming concepts, structured data handling, file
persistence, and defensive programming through exception handling.

## 2. Objective

The objectives of this project are:

1. To design and implement a fully functional student record management
   application using core Python (no external database engine).
2. To organize the program using well-defined, reusable functions rather
   than a single block of procedural code.
3. To store structured student data (ID, Name, Age, Course, Marks) using
   Python's built-in data structures (lists of dictionaries) and persist
   that data to disk using JSON.
4. To validate all user input and handle runtime errors gracefully so the
   program never crashes on invalid input or missing/corrupted files.
5. To present data to the user in a clean, readable, tabular format.
6. To apply good coding practices — meaningful names, docstrings, inline
   comments, and PEP 8 formatting — throughout the codebase.

## 3. System Design

### 3.1 Overview

The system follows a simple **menu-driven, function-based architecture**.
The `main()` function loads existing data, then repeatedly displays a
menu and dispatches the user's choice to the appropriate function until
the user selects *Exit*.

### 3.2 Data Model

Each student record is represented as a Python dictionary with five
fields:

| Field  | Type  | Description                    |
|--------|-------|---------------------------------|
| ID     | int   | Unique identifier for a student |
| Name   | str   | Full name of the student        |
| Age    | int   | Age of the student               |
| Course | str   | Enrolled course/program          |
| Marks  | float | Academic marks/score             |

All records are held together in a single list (`records`), making the
in-memory structure a *list of dictionaries* — a lightweight, flexible
substitute for a database table, where the list is the table and each
dictionary is a row.

### 3.3 Persistence Design

Data persistence is handled through two dedicated functions:

- `load_from_file()` — reads `records.json` at program startup and
  returns its contents as a list of dictionaries. If the file is
  missing, empty, or corrupted, it safely returns an empty list instead
  of crashing.
- `save_to_file(records)` — writes the current in-memory list back to
  `records.json` in a human-readable, indented format. This is called
  immediately after every add, update, or delete operation so that data
  on disk always reflects the latest state.

### 3.4 Module / Function Breakdown

```
main.py
├── load_from_file()          → reads records.json into memory
├── save_to_file()             → writes in-memory records to records.json
├── get_non_empty_string()     → validated text input helper
├── get_valid_integer()        → validated integer input helper
├── get_valid_float()          → validated decimal input helper
├── find_record_index_by_id()  → locates a record's position by ID
├── add_record()                → creates a new record
├── view_records()              → displays all records in a table
├── search_record()             → finds records by ID or Name
├── update_record()             → edits an existing record's fields
├── delete_record()             → removes a record after confirmation
├── display_menu()              → prints the menu options
└── main()                      → program entry point / control loop
```

This separation of concerns means each function has a single, clear
responsibility, which makes the program easy to read, test, and extend.

### 3.5 Program Flow

1. Program starts → `load_from_file()` loads any existing records.
2. `main()` enters an infinite loop, calling `display_menu()` each time.
3. The user's numeric choice (1–6) is captured and validated.
4. The matching function (`add_record`, `view_records`, `search_record`,
   `update_record`, or `delete_record`) is called.
5. Any change to the data is immediately saved via `save_to_file()`.
6. Choosing option 6 breaks the loop and ends the program.

## 4. Python Concepts Used

This project applies a range of core Python concepts learned in the
course:

- **Functions and modular design** — every operation is isolated into
  its own function, following the single-responsibility principle.
- **Lists and dictionaries** — student records are modeled as a *list of
  dictionaries*, Python's natural equivalent of a table of rows.
- **File handling (I/O)** — the built-in `open()` function, used with
  `with` statements, safely reads and writes the `records.json` file.
- **The `json` module** — `json.load()` and `json.dump()` convert
  between Python objects and JSON text for persistent storage.
- **Exception handling** — `try`/`except` blocks catch `ValueError`
  (bad numeric input), `FileNotFoundError` and `json.JSONDecodeError`
  (missing/corrupted data file), and `IOError`/`OSError` (file write
  failures), ensuring the program degrades gracefully instead of
  crashing.
- **Loops (`while`, `for`)** — `while` loops power the input-validation
  helpers and the main menu loop; `for` loops iterate over records when
  searching or displaying them.
- **Conditional statements** — `if`/`elif`/`else` drive menu dispatch and
  field-by-field validation logic.
- **List comprehensions** — used in `search_record()` to filter matching
  records concisely.
- **String formatting (f-strings)** — used extensively for clean,
  aligned tabular output and dynamic messages.
- **Control flow with `break`/`continue`** — used inside validation
  loops to exit once valid input is received.

## 5. Feature Summary

| # | Feature                          | Description                                                              |
|---|-----------------------------------|---------------------------------------------------------------------------|
| 1 | Add Record                        | Add a new student with a unique ID; duplicate IDs are rejected.          |
| 2 | View All Records                  | Displays every record in a neatly aligned table.                         |
| 3 | Search Record (ID or Name)        | Search by exact ID or partial, case-insensitive name match.              |
| 4 | Update Record                     | Edit any field of an existing record; blank input keeps the old value.   |
| 5 | Delete Record                     | Remove a record by ID, with a y/n confirmation prompt.                   |
| 6 | Exit                                | Cleanly ends the program loop.                                            |
| 7 | Persistent JSON Storage           | All changes are saved to `records.json` automatically.                   |
| 8 | Input Validation Loops            | Invalid input never crashes the program; the user is re-prompted.        |
| 9 | Duplicate ID Prevention           | The system blocks adding a record with an already-used ID.               |
| 10| Graceful File-Error Handling      | Missing or corrupted `records.json` is handled without crashing.         |

## 6. Testing

The application was tested manually by simulating a full end-to-end user
session covering every menu option, in the following sequence:

1. **Add Record** — added two students (IDs 101 and 102) with valid
   details. *Result:* both records were created and correctly written
   to `records.json`.
2. **Duplicate ID check** — attempted to add a new record using ID 101
   again. *Result:* the system displayed an error and re-prompted for a
   different ID, without corrupting existing data.
3. **View All Records** — displayed the full list. *Result:* records
   were shown in a clean, aligned table with the correct total count.
4. **Search Record** — searched by ID (102) and by partial Name.
   *Result:* correct matching record(s) were returned; a search with no
   match correctly reported "No matching record(s) found."
5. **Update Record** — updated the Name field of ID 102 while leaving
   Age, Course, and Marks blank. *Result:* only the Name field changed;
   all other fields kept their original values, and the change was
   saved to disk.
6. **Delete Record** — deleted ID 101 after confirming with `y`.
   *Result:* the record was removed from memory and from
   `records.json`, and the total record count updated correctly.
7. **Invalid input handling** — entered non-numeric text (e.g. `abc`)
   at the menu prompt and at numeric fields such as Age and Marks.
   *Result:* the program printed a clear error message and re-prompted
   instead of crashing.
8. **Missing/corrupted file handling** — tested startup behavior with
   `records.json` deleted, and separately with the file containing
   invalid JSON text. *Result:* in both cases the program printed a
   warning and started with an empty record list rather than raising an
   unhandled exception.
9. **Exit** — selected option 6. *Result:* the program printed a
   goodbye message and terminated the loop cleanly.

All test cases passed, confirming that the application behaves
correctly under both normal and erroneous conditions, and that data
persists correctly across program restarts.

## 7. Conclusion

The Student Record Management System successfully meets all the stated
objectives: it provides a complete, menu-driven interface for managing
student records; it is built entirely from small, well-documented
functions rather than one large script; it persists data reliably using
JSON file storage; and it validates user input and handles file/runtime
errors gracefully at every step.

Building this project reinforced practical, hands-on understanding of
core Python concepts — functions, data structures, file I/O, the `json`
module, and exception handling — and demonstrated how these concepts
combine to produce a small but genuinely usable data-management tool.
While the current version uses a JSON file for storage, the same
function-based design (particularly `load_from_file` and
`save_to_file`) could be adapted in the future to use a relational
database such as SQLite or MySQL with minimal changes to the rest of
the program, making this project a solid foundation for further study
of relational databases.
