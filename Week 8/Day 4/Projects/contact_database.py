# Contact database with structured contact information saved to a json file.

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, company, phone, email):
    """Add a new contact and save to file."""
    contacts = load_contacts()
    contact = {
        "name": name,
        "company": company,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts(contacts)

def get_contacts():
    """Return all contacts."""
    return load_contacts()

# Example usage:
if __name__ == "__main__":
    add_contact("Alice Smith", "Acme Corp", "555-1234", "alice@acme.com")
    add_contact("Bob Jones", "Beta LLC", "555-5678", "bob@beta.com")
    print(get_contacts())

