contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print(" No contacts found.\n")
        return
    print("\nContact List:")
    for contact in contacts:
        print(f" {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    phone = input("Enter phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Contact found. Enter new details.")
            contact['name'] = input("New name: ")
            contact['email'] = input("New email: ")
            contact['address'] = input("New address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    print("Welcome to Contact Management System")
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book")
            break
        else:
            print("Invalid choice. Please try again")
main()
