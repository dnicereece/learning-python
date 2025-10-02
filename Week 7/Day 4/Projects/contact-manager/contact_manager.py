# Contact Manager Application that loads and saves contact information to files as dictionary data

# Import necessary modules
import json # for handling JSON data
import os # for file path operations

# Function to load contacts from a file
def load_contacts(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            contacts = json.load(file)
            return contacts
    else:
        return {}
    
# Function to save contacts to a file
def save_contacts(file_path, contacts):
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts, name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    return contacts

# Function to display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Main function to run the contact manager
def main():
    file_path = 'contacts.json'
    contacts = load_contacts(file_path)
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contacts = add_contact(contacts, name, phone, email)
            print(f"Contact {name} added.")
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            save_contacts(file_path, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()