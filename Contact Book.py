#  Project: Contact Book (CLI)
#  Description:
# Save, view, search, delete contacts.
# Store data in a file (contacts.txt).
# Handle invalid input with exceptions.
# Use functions and maybe your own module!

# Features:
# Add New Contact
# View All Contacts
# Search by Name
# Delete Contact
# Exit


def add_contact():
    name = input("Name: ")
    phone = int(input("Phone: "))
    with open('contacts.txt', 'a') as file:
        file.write(f"{name},{phone}\n")

def view_contacts():
    try:
        with open('contacts.txt', 'r') as file:
            contacts = file.readlines()
            for contact in contacts:
                name, phone = contact.strip().split(',')
                print(f"Name:{name},Phone:{phone}")
    except FileNotFoundError:
        print("No Contact Yet!")

def search_contact():
    search = input("Enter name to search: ")
    found = False
    with open('contacts.txt', 'r') as file:
        for line in file:
            name, phone = line.strip().split(',')
            if name.lower() == search.lower():
                print(f"Found: {name} - {phone}")
                found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    name_to_delete = input("Enter name to delect: ")
    contacts = []
    deleted = False
    with open('contacts.txt', 'r') as file:
        contacts =  file.readlines()
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            name, phone = contact.strip().split(',')
            if name.lower() != name_to_delete.lower():
                file.write(contact)
            else:
                deleted = True
    if deleted:
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact\n2. View Contact\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("choice option: ")
        try:
            if choice == '1':
                add_contact()
            elif choice == '2':
                view_contacts()
            elif choice == '3':
                search_contact()
            elif choice == '4':
                delete_contact()
            elif choice == '5':
                print("Good Bye!")
                break
            else:
                print("Invalid Choice!")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
