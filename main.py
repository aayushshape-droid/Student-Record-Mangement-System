"""
Student Record Management System
==================================

A menu-driven console application to manage student records
(ID, Name, Age, Course, Marks). Records are stored in memory as a
list of dictionaries and persisted to a JSON file (records.json)
so that data survives after the program closes.

Author : Claude
"""

import json
import os

# Name of the JSON file used to persist student records.
DATA_FILE = "records.json"


# --------------------------------------------------------------------------
# FILE I/O FUNCTIONS
# --------------------------------------------------------------------------

def load_from_file():
    """
    Load student records from the JSON data file.

    Returns:
        list: A list of dictionaries, each representing a student record.
              Returns an empty list if the file does not exist, is empty,
              or contains invalid JSON.
    """
    # If the file does not exist yet, there is nothing to load.
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file_handle:
            data = json.load(file_handle)
            # Guard against a corrupted file that doesn't hold a list.
            if isinstance(data, list):
                return data
            print("Warning: records.json did not contain a list. Starting fresh.")
            return []
    except FileNotFoundError:
        # Should not normally happen because of the os.path.exists check,
        # but handled defensively as required.
        print("No existing data file found. Starting with an empty record set.")
        return []
    except json.JSONDecodeError:
        # The file exists but its content is not valid JSON (e.g. empty
        # or corrupted file).
        print("Warning: records.json is corrupted or empty. Starting fresh.")
        return []


def save_to_file(records):
    """
    Save the current list of student records to the JSON data file.

    Args:
        records (list): The list of student record dictionaries to save.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file_handle:
            json.dump(records, file_handle, indent=4)
    except (IOError, OSError) as error:
        # Catches issues like permission denied or disk full.
        print(f"Error: Could not save data to file. Details: {error}")


# --------------------------------------------------------------------------
# INPUT VALIDATION HELPERS
# --------------------------------------------------------------------------

def get_non_empty_string(prompt):
    """
    Repeatedly prompt the user until a non-empty string is entered.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        str: A validated, non-empty, stripped string.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_integer(prompt):
    """
    Repeatedly prompt the user until a valid integer is entered.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        int: A validated integer value.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt):
    """
    Repeatedly prompt the user until a valid float (marks) is entered.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        float: A validated float value.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 85 or 85.5).")


# --------------------------------------------------------------------------
# CORE RECORD OPERATIONS
# --------------------------------------------------------------------------

def find_record_index_by_id(records, student_id):
    """
    Find the index of a record in the list by its student ID.

    Args:
        records (list): The list of student record dictionaries.
        student_id (int): The ID to search for.

    Returns:
        int: The index of the matching record, or -1 if not found.
    """
    for index, record in enumerate(records):
        if record["ID"] == student_id:
            return index
    return -1


def add_record(records):
    """
    Prompt the user for details of a new student and add it to the
    records list, then persist the updated list to disk.

    Args:
        records (list): The list of student record dictionaries.
    """
    print("\n--- Add New Student Record ---")

    # Keep asking for an ID until a unique one is provided.
    while True:
        student_id = get_valid_integer("Enter Student ID: ")
        if find_record_index_by_id(records, student_id) != -1:
            print(f"Error: A record with ID {student_id} already exists. "
                  "Please enter a different ID.")
        else:
            break

    name = get_non_empty_string("Enter Student Name: ")
    age = get_valid_integer("Enter Student Age: ")
    course = get_non_empty_string("Enter Course: ")
    marks = get_valid_float("Enter Marks: ")

    # Build the new record as a dictionary and append it to the list.
    new_record = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks,
    }
    records.append(new_record)

    # Persist changes immediately so data is never lost.
    save_to_file(records)
    print(f"Record for '{name}' (ID: {student_id}) added successfully.\n")


def view_records(records):
    """
    Display all student records in a clean tabular format.

    Args:
        records (list): The list of student record dictionaries.
    """
    print("\n--- All Student Records ---")

    if not records:
        print("No records found.\n")
        return

    # Column widths for a neatly aligned table.
    header_format = f"{'ID':<8}{'Name':<20}{'Age':<6}{'Course':<20}{'Marks':<8}"
    print(header_format)
    print("-" * len(header_format))

    for record in records:
        row = (f"{record['ID']:<8}{record['Name']:<20}{record['Age']:<6}"
               f"{record['Course']:<20}{record['Marks']:<8}")
        print(row)

    print(f"\nTotal records: {len(records)}\n")


def search_record(records):
    """
    Search for a student record by either ID or Name, based on the
    user's choice, and display any matches.

    Args:
        records (list): The list of student record dictionaries.
    """
    print("\n--- Search Student Record ---")
    print("1. Search by ID")
    print("2. Search by Name")

    choice = get_valid_integer("Enter your choice (1 or 2): ")

    matches = []
    if choice == 1:
        student_id = get_valid_integer("Enter Student ID to search: ")
        matches = [record for record in records if record["ID"] == student_id]
    elif choice == 2:
        name_query = get_non_empty_string("Enter Student Name to search: ")
        # Case-insensitive partial match on name for a friendlier search.
        matches = [record for record in records
                   if name_query.lower() in record["Name"].lower()]
    else:
        print("Invalid choice. Returning to main menu.\n")
        return

    if not matches:
        print("No matching record(s) found.\n")
        return

    header_format = f"{'ID':<8}{'Name':<20}{'Age':<6}{'Course':<20}{'Marks':<8}"
    print(header_format)
    print("-" * len(header_format))
    for record in matches:
        row = (f"{record['ID']:<8}{record['Name']:<20}{record['Age']:<6}"
               f"{record['Course']:<20}{record['Marks']:<8}")
        print(row)
    print()


def update_record(records):
    """
    Update the details of an existing student record identified by ID.

    Args:
        records (list): The list of student record dictionaries.
    """
    print("\n--- Update Student Record ---")
    student_id = get_valid_integer("Enter the Student ID to update: ")
    index = find_record_index_by_id(records, student_id)

    if index == -1:
        print(f"No record found with ID {student_id}.\n")
        return

    record = records[index]
    print(f"Current details: {record}")
    print("Leave a field blank to keep its current value.\n")

    # Name: allow blank input to keep the existing value.
    new_name = input(f"Enter new Name [{record['Name']}]: ").strip()
    if new_name:
        record["Name"] = new_name

    # Age: allow blank input, otherwise validate as integer.
    while True:
        new_age_raw = input(f"Enter new Age [{record['Age']}]: ").strip()
        if not new_age_raw:
            break
        try:
            record["Age"] = int(new_age_raw)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number or leave blank.")

    # Course: allow blank input to keep the existing value.
    new_course = input(f"Enter new Course [{record['Course']}]: ").strip()
    if new_course:
        record["Course"] = new_course

    # Marks: allow blank input, otherwise validate as float.
    while True:
        new_marks_raw = input(f"Enter new Marks [{record['Marks']}]: ").strip()
        if not new_marks_raw:
            break
        try:
            record["Marks"] = float(new_marks_raw)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value or leave blank.")

    # Save the updated record back into the list and persist to disk.
    records[index] = record
    save_to_file(records)
    print(f"Record with ID {student_id} updated successfully.\n")


def delete_record(records):
    """
    Delete an existing student record identified by ID, after
    confirmation from the user.

    Args:
        records (list): The list of student record dictionaries.
    """
    print("\n--- Delete Student Record ---")
    student_id = get_valid_integer("Enter the Student ID to delete: ")
    index = find_record_index_by_id(records, student_id)

    if index == -1:
        print(f"No record found with ID {student_id}.\n")
        return

    record = records[index]
    confirm = input(f"Are you sure you want to delete '{record['Name']}' "
                     f"(ID: {student_id})? (y/n): ").strip().lower()

    if confirm == "y":
        del records[index]
        save_to_file(records)
        print("Record deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")


# --------------------------------------------------------------------------
# MENU / MAIN PROGRAM LOOP
# --------------------------------------------------------------------------

def display_menu():
    """Print the main menu options to the console."""
    print("=" * 40)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record (by ID or Name)")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("=" * 40)


def main():
    """Main program loop: load data, show menu, dispatch to operations."""
    # Load any existing records from disk when the program starts.
    records = load_from_file()

    while True:
        display_menu()
        choice = get_valid_integer("Enter your choice (1-6): ")

        if choice == 1:
            add_record(records)
        elif choice == 2:
            view_records(records)
        elif choice == 3:
            search_record(records)
        elif choice == 4:
            update_record(records)
        elif choice == 5:
            delete_record(records)
        elif choice == 6:
            print("Exiting Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
