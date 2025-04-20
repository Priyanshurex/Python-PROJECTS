import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                for contact_data in data:
                    contact = Contact(contact_data['name'], contact_data['phone'], contact_data['email'], contact_data['address'])
                    self.contacts.append(contact)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            data = []
            for contact in self.contacts:
                contact_data = {
                    'name': contact.name,
                    'phone': contact.phone,
                    'email': contact.email,
                    'address': contact.address
                }
                data.append(contact_data)
            json.dump(data, file)

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {i}:\n{contact}")

    def search_contact(self, query):
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                contact.address = address
                self.save_contacts()
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            manager.update_contact(name, phone, email, address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
