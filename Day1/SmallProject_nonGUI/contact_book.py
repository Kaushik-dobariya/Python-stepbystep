# Contact book application
contacts = [] # List to store contact information
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact=(name, phone)
    contacts.append(contact)
    print("✅ Contact added successfully!\n")
    
def view_contacts():
    if not contacts or len(contacts) == 0:
        print("❌ No contacts found..!\n")
    else:
        print("Contact List:")
        for contact in contacts:    
            print(f"Name: {contact[0]}, Phone: {contact[1]}")

def search_contact():
    search_name = input("Enter contact name to search: ")

    found_contacts = [contact for contact in contacts if contact[0].lower() == search_name.lower()]
    if found_contacts:
        print("Contact(s) found:")
        for contact in found_contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}")
    else:
       print("❌ Contact not found.\n")
       
def delete_contact():
    delete_name = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact[0].lower() == delete_name.lower():
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!\n")
            return
    print("❌ Contact not found.\n")
    
# Main Menu Loop
while True:
    print("===== 📒 Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.\n")  