# Task
# Develop an information system Employees.
# The app should provide data input, editing
# the employee's data, deleting an employee, '
# 'searching for an employee by last name, outputting'
# ' information about all employees of the specified '
# 'age or whose last name begins with the specified letter. '
# 'Provide the possibility to save the found information to a file. '
# 'The full list of employees is also saved to a file (automatically '
# 'when exiting the app, by the user's command at runtime).
# The employee list is loaded from the file specified by the
# user when the app starts.




#!/usr/bin/env python3
"""
employees_app.py

Employees information system (console app).

Features:
- Load employee list from a JSON file specified by the user at startup.
- Add, edit, delete employees.
- Search by last name (case-insensitive substring).
- Filter by age or by last name starting letter.
- Save search results to a file.
- Save full list automatically on exit, or manually at runtime.

Data format (JSON): a list of employee dicts:
[
  {
    "id": 1,
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "position": "Engineer",
    "email": "alice@example.com",
    "phone": "555-0123"
  },
  ...
]
"""

import json
import os
import sys
from typing import List, Dict, Optional

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def load_employees_from_file(path: str) -> List[Dict]:
    if not os.path.exists(path):
        # Create empty file
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2)
        return []
    with open(path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                # Basic sanity: ensure all entries have id
                return data
            else:
                print("File content invalid (not a list). Starting with empty list.")
                return []
        except json.JSONDecodeError:
            print("File is not valid JSON. Starting with empty list.")
            return []

def save_employees_to_file(path: str, employees: List[Dict]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(employees, f, indent=2, ensure_ascii=False)

def next_id(employees: List[Dict]) -> int:
    if not employees:
        return 1
    return max((e.get('id', 0) for e in employees), default=0) + 1

def print_employee(e: Dict) -> None:
    print(f"ID: {e.get('id')}\tName: {e.get('first_name')} {e.get('last_name')}\tAge: {e.get('age')}\tPosition: {e.get('position')}\tEmail: {e.get('email')}\tPhone: {e.get('phone')}")

def list_all(employees: List[Dict]) -> None:
    if not employees:
        print("No employees to show.")
        return
    print(f"Listing all {len(employees)} employees:")
    for e in employees:
        print_employee(e)

def input_nonempty(prompt: str, default: Optional[str]=None) -> str:
    while True:
        if default is None:
            val = input(prompt).strip()
        else:
            val = input(f"{prompt} [{default}]: ").strip()
            if val == '':
                return default
        if val == '':
            print("Input cannot be empty.")
        else:
            return val

def input_int(prompt: str, default: Optional[int]=None, allow_empty=False) -> Optional[int]:
    while True:
        if default is None and not allow_empty:
            s = input(prompt).strip()
        elif default is not None:
            s = input(f"{prompt} [{default}]: ").strip()
            if s == '':
                return default
        else:
            s = input(prompt).strip()
            if s == '' and allow_empty:
                return None

        try:
            return int(s)
        except ValueError:
            print("Please enter an integer value.")

def add_employee(employees: List[Dict]) -> None:
    print("\nAdd new employee")
    fid = next_id(employees)
    first = input_nonempty("First name: ")
    last = input_nonempty("Last name: ")
    age = input_int("Age: ")
    position = input_nonempty("Position: ")
    email = input_nonempty("Email: ")
    phone = input_nonempty("Phone: ")
    new = {
        "id": fid,
        "first_name": first,
        "last_name": last,
        "age": age,
        "position": position,
        "email": email,
        "phone": phone
    }
    employees.append(new)
    print("Employee added:")
    print_employee(new)

def find_by_id(employees: List[Dict], id_value: int) -> Optional[Dict]:
    for e in employees:
        if e.get('id') == id_value:
            return e
    return None

def edit_employee(employees: List[Dict]) -> None:
    print("\nEdit employee")
    idv = input_int("Enter employee ID to edit: ")
    emp = find_by_id(employees, idv)
    if not emp:
        print(f"No employee with ID {idv}.")
        return
    print("Current data:")
    print_employee(emp)
    print("\nEnter new values (leave empty to keep current).")
    fn = input(f"First name [{emp['first_name']}]: ").strip() or emp['first_name']
    ln = input(f"Last name [{emp['last_name']}]: ").strip() or emp['last_name']
    age = input_int("Age: ", default=emp['age'])
    pos = input(f"Position [{emp['position']}]: ").strip() or emp['position']
    email = input(f"Email [{emp['email']}]: ").strip() or emp['email']
    phone = input(f"Phone [{emp['phone']}]: ").strip() or emp['phone']
    emp.update({
        'first_name': fn,
        'last_name': ln,
        'age': age,
        'position': pos,
        'email': email,
        'phone': phone
    })
    print("Employee updated:")
    print_employee(emp)

def delete_employee(employees: List[Dict]) -> None:
    print("\nDelete employee")
    idv = input_int("Enter employee ID to delete: ")
    emp = find_by_id(employees, idv)
    if not emp:
        print(f"No employee with ID {idv}.")
        return
    print("About to delete:")
    print_employee(emp)
    c = input("Type 'yes' to confirm deletion: ").strip().lower()
    if c == 'yes':
        employees.remove(emp)
        print("Employee deleted.")
    else:
        print("Deletion cancelled.")

def search_by_last_name(employees: List[Dict]) -> List[Dict]:
    print("\nSearch by last name")
    name = input_nonempty("Enter last name (or substring) to search (case-insensitive): ")
    matches = [e for e in employees if name.lower() in e.get('last_name','').lower()]
    if not matches:
        print("No matches found.")
    else:
        print(f"Found {len(matches)} matching employee(s):")
        for e in matches:
            print_employee(e)
    return matches

def filter_by_age(employees: List[Dict]) -> List[Dict]:
    print("\nFilter by age")
    age = input_int("Enter age to filter by: ")
    matches = [e for e in employees if e.get('age') == age]
    if not matches:
        print("No employees of that age.")
    else:
        print(f"Employees aged {age}:")
        for e in matches:
            print_employee(e)
    return matches

def filter_by_lastname_initial(employees: List[Dict]) -> List[Dict]:
    print("\nFilter by last name initial")
    while True:
        s = input("Enter a single letter (last-name should begin with this letter): ").strip()
        if len(s) == 1 and s.isalpha():
            letter = s.lower()
            break
        print("Please enter a single alphabetic character.")
    matches = [e for e in employees if e.get('last_name','').lower().startswith(letter)]
    if not matches:
        print(f"No employees with last names starting with '{letter}'.")
    else:
        print(f"Employees whose last name starts with '{letter}':")
        for e in matches:
            print_employee(e)
    return matches

def save_search_results(results: List[Dict]) -> None:
    if not results:
        print("No results to save.")
        return
    path = input_nonempty("Enter filename to save results (e.g. results.json): ")
    # If extension not provided, add .json
    if not os.path.splitext(path)[1]:
        path += '.json'
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(results)} records to '{path}'.")
    except Exception as exc:
        print(f"Failed to save file: {exc}")

def manual_save_full_list(employees: List[Dict], file_path: str) -> None:
    try:
        save_employees_to_file(file_path, employees)
        print(f"Full employee list saved to '{file_path}'.")
    except Exception as exc:
        print(f"Failed to save full list: {exc}")

def show_menu():
    clear_screen()
    print("=== Employees Information System ===")
    print("1) List all employees")
    print("2) Add new employee")
    print("3) Edit existing employee")
    print("4) Delete employee")
    print("5) Search by last name")
    print("6) Filter by age")
    print("7) Filter by last-name initial")
    print("8) Save full list now")
    print("9) Save last shown search/filter results to file")
    print("0) Exit")
    print("====================================")

def main():
    print("Employees information system — startup")
    file_path = input_nonempty("Enter path to employee JSON file to load (will be created if missing): ")
    if not file_path.lower().endswith('.json'):
        # still allow non-json filename but we prefer .json
        pass
    employees = load_employees_from_file(file_path)
    last_results: List[Dict] = []  # store last search/filter result for saving
    try:
        while True:
            show_menu()
            choice = input("Choose an option: ").strip()
            if choice == '1':
                clear_screen()
                list_all(employees)
                last_results = employees.copy()
                pause()
            elif choice == '2':
                clear_screen()
                add_employee(employees)
                last_results = []
                pause()
            elif choice == '3':
                clear_screen()
                edit_employee(employees)
                last_results = []
                pause()
            elif choice == '4':
                clear_screen()
                delete_employee(employees)
                last_results = []
                pause()
            elif choice == '5':
                clear_screen()
                last_results = search_by_last_name(employees)
                pause()
            elif choice == '6':
                clear_screen()
                last_results = filter_by_age(employees)
                pause()
            elif choice == '7':
                clear_screen()
                last_results = filter_by_lastname_initial(employees)
                pause()
            elif choice == '8':
                clear_screen()
                manual_save_full_list(employees, file_path)
                pause()
            elif choice == '9':
                clear_screen()
                save_search_results(last_results)
                pause()
            elif choice == '0':
                print("Exiting... saving full list...")
                # Save before exit
                save_employees_to_file(file_path, employees)
                print(f"Full list saved to '{file_path}'. Goodbye.")
                return
            else:
                print("Unknown option. Try again.")
                pause()
    except (KeyboardInterrupt, EOFError):
        # Ensure save on abrupt exit (Ctrl+C / Ctrl+D)
        print("\nInterrupted. Saving full list before exit...")
        try:
            save_employees_to_file(file_path, employees)
            print(f"Saved to '{file_path}'.")
        except Exception as exc:
            print("Failed to save on exit:", exc)
        print("Goodbye.")
        return

if __name__ == "__main__":
    main()
