# Contact Manager application with backup and restore functionality

import json
import os
import re

CONTACTS_FILE = "contacts.json"
BACKUP_FILE = "contacts_backup.json"

def read_contacts(file=CONTACTS_FILE):
    """
    Reads contacts from the specified JSON file.
    Returns a list of contacts or an empty list if file is missing or invalid.
    """
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {file} contains invalid data.")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    return []

def write_contacts(contacts, file=CONTACTS_FILE):
    """
    Writes the contacts list to the specified JSON file in a readable format.
    """
    try:
        with open(file, "w") as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def backup_contacts():
    """
    Creates a backup of the contacts file.
    """
    try:
        write_contacts(read_contacts(), BACKUP_FILE)
        print("Backup created successfully.")
    except Exception as e:
        print(f"Backup failed: {e}")

def restore_contacts():
    """
    Restores contacts from the backup file.
    """
    try:
        write_contacts(read_contacts(BACKUP_FILE))
        print("Contacts restored from backup.")
    except Exception as e:
        print(f"Restore failed: {e}")

def export_contacts(export_file):
    """
    Exports contacts to a user-specified file.
    """
    try:
        write_contacts(read_contacts(), export_file)
        print(f"Contacts exported to {export_file}.")
    except Exception as e:
        print(f"Export failed: {e}")

def import_contacts(import_file):
    """
    Imports contacts from a user-specified file.
    """
    try:
        write_contacts(read_contacts(import_file))
        print(f"Contacts imported from {import_file}.")
    except Exception as e:
        print(f"Import failed: {e}")

def validate_name(name):
    """
    Converts a name to title case.
    """
    return name.title()

def validate_phone(phone):
    """
    Validates phone number format.
    Accepts formats like 123-456-7890, (123) 456-7890, 1234567890.
    """
    pattern = r'^(\(\d{3}\)\s?|\d{3}[-\s]?)?\d{3}[-\s]?\d{4}$'
    return re.match(pattern, phone)

def validate_email(email):
    """
    Validates basic email format.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def get_validated_input(field):
    """
    Prompts user for input and validates it based on the field type.
    """
    while True:
        value = input(f"Enter {field}: ")
        if field == "name":
            return validate_name(value)
        elif field == "phone":
            if validate_phone(value): return value
            print("Invalid phone number format.")
        elif field == "email":
            if validate_email(value): return value
            print("Invalid email format.")
        else:
            return value

def view_contacts():
    """
    Displays all contacts in the contacts file.
    """
    contacts = read_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. Name: {c['name']}, Company: {c['company']}, Phone: {c['phone']}, Email: {c['email']}")

def add_contact():
    """
    Adds a new contact after validating user input.
    """
    name = get_validated_input("name")
    company = get_validated_input("company")
    phone = get_validated_input("phone")
    email = get_validated_input("email")
    contacts = read_contacts()
    contacts.append({"name": name, "company": company, "phone": phone, "email": email})
    write_contacts(contacts)
    print("Contact added.")

def edit_contact(index, field):
    """
    Edits a specific field of a contact at the given index.
    """
    contacts = read_contacts()
    if 0 <= index < len(contacts):
        value = get_validated_input(field)
        contacts[index][field] = value
        write_contacts(contacts)
        print("Contact updated.")
    else:
        print("Invalid contact index.")

def remove_contact(index):
    """
    Removes a contact at the given index.
    """
    contacts = read_contacts()
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        write_contacts(contacts)
        print(f"Removed contact: {removed['name']}")
    else:
        print("Invalid contact index.")

def search_contacts_field(field, query):
    """
    Searches contacts by a specific field and query string.
    """
    contacts = read_contacts()
    results = [c for c in contacts if query.lower() in c[field].lower()]
    if results:
        for c in results:
            print(f"Name: {c['name']}, Company: {c['company']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("No matching contacts found.")

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print("\nContact Manager Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Remove Contact")
        print("5. Search Contacts")
        print("6. Export Contacts")
        print("7. Import Contacts")
        print("8. Backup Contacts")
        print("9. Restore Contacts")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
            try:
                idx = int(input("Enter contact number to edit: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            fields = {"1": "name", "2": "company", "3": "phone", "4": "email"}
            print("\nEdit Contact:\n1. Name\n2. Company\n3. Phone\n4. Email\n0. Cancel")
            f_choice = input("Select field to edit: ")
            if f_choice in fields:
                edit_contact(idx, fields[f_choice])
            elif f_choice == "0":
                print("Edit cancelled.")
            else:
                print("Invalid option.")
        elif choice == "4":
            view_contacts()
            try:
                idx = int(input("Enter contact number to remove: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            remove_contact(idx)
        elif choice == "5":
            fields = {"1": "name", "2": "company", "3": "phone", "4": "email"}
            print("\nSearch Contacts:\n1. Name\n2. Company\n3. Phone\n4. Email\n0. Cancel")
            f_choice = input("Select field to search: ")
            if f_choice in fields:
                query = input(f"Enter {fields[f_choice]} to search: ")
                search_contacts_field(fields[f_choice], query)
            elif f_choice == "0":
                print("Search cancelled.")
            else:
                print("Invalid option.")
        elif choice == "6":
            export_file = input("Enter export filename: ")
            export_contacts(export_file)
        elif choice == "7":
            import_file = input("Enter import filename: ")
            import_contacts(import_file)
        elif choice == "8":
            backup_contacts()
        elif choice == "9":
            restore_contacts()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
