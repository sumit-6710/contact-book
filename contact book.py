contacts = []


def add_contact():
    print("\n--- Add Contact ---")

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append([name, phone, email, address])

    print("Contact saved successfully!")


def show_contacts():
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts available.")
        return

    for i in range(len(contacts)):
        print(f"\nContact {i + 1}")
        print("Name:", contacts[i][0])
        print("Phone:", contacts[i][1])
        print("Email:", contacts[i][2])
        print("Address:", contacts[i][3])


def find_contact():
    print("\n--- Search Contact ---")

    value = input("Enter name or phone: ").lower()

    for contact in contacts:
        if value in contact[0].lower() or value in contact[1]:
            print("\nName:", contact[0])
            print("Phone:", contact[1])
            print("Email:", contact[2])
            print("Address:", contact[3])
            return

    print("Contact not found.")


def change_contact():
    print("\n--- Update Contact ---")

    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact[0].lower() == name:
            contact[0] = input("New name: ")
            contact[1] = input("New phone: ")
            contact[2] = input("New email: ")
            contact[3] = input("New address: ")

            print("Contact updated!")
            return

    print("Contact not found.")


def remove_contact():
    print("\n--- Delete Contact ---")

    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact[0].lower() == name:
            contacts.remove(contact)
            print("Contact deleted!")
            return

    print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        find_contact()

    elif choice == "4":
        change_contact()

    elif choice == "5":
        remove_contact()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Please enter a valid option.")