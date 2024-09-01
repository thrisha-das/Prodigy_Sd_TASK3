# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:18:36 2024

@author: THRISHA DAS
"""

import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        contact = contacts[index]
        print(f"Editing contact: {contact['name']}")
        contact['name'] = input(f"Enter new name (leave blank to keep '{contact['name']}'): ").strip() or contact['name']
        contact['phone'] = input(f"Enter new phone number (leave blank to keep '{contact['phone']}'): ").strip() or contact['phone']
        contact['email'] = input(f"Enter new email address (leave blank to keep '{contact['email']}'): ").strip() or contact['email']
        save_contacts(contacts)
        print("Contact updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    