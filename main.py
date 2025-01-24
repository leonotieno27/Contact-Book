import os
import sys

filename = 'contacts.txt'

class Contacts:
    def __init__(self, fname, lname, phone_number, email):
        self.fname = fname
        self.lname = lname
        self.phone_number = phone_number
        self.email = email

    def store_names(self):
        """Stores user's details."""
        with open(filename, 'a') as file_object:
            file_object.write(f"{self.fname}|{self.lname}|{self.phone_number}|{self.email}\n")

    @staticmethod
    def search_names(target):
        """Searches contacts by phone number."""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        content.sort(key=lambda line: line.split('|')[2])  # Sort by phone number

        # Binary search
        left, right = 0, len(content) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_phone = content[mid].split('|')[2]

            if mid_phone == target:
                fname, lname, phone_number, email = content[mid].strip().split('|')
                print("\nContact Found:")
                print(f"Name: {fname} {lname}")
                print(f"Phone: {phone_number}")
                print(f"Email: {email}")
                return
            elif mid_phone < target:
                left = mid + 1
            else:
                right = mid - 1

        print("Contact not found.")

    @staticmethod
    def view_names():
        """Displays all saved contacts."""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        if content:
            print("\t\t\t*** Saved Contacts ***\n")
            for line in sorted(content):  # Sort alphabetically by name
                fname, lname, phone_number, email = line.strip().split('|')
                print(f"Name: {fname} {lname}, Phone: {phone_number}, Email: {email}")
        else:
            print("No contacts found.")

    @staticmethod
    def delete_contacts(target):
        """Deletes a contact by phone number."""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        new_content = [line for line in content if line.split('|')[2] != target] #if phone number is not equal to new number

        if len(content) == len(new_content):
            print("Contact not found.")
        else:
            with open(filename, 'w') as file_object:
                file_object.writelines(new_content)
            print("Contact deleted successfully.")

    @staticmethod
    def update_contacts(target):
        """Updates a contact by phone number."""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        updated = False
        for i, line in enumerate(content):  #iterate through the list
            if line.split('|')[2] == target:
                print("\nContact Found:")
                fname, lname, phone_number, email = line.strip().split('|')
                print(f"Name: {fname} {lname}, Phone: {phone_number}, Email: {email}")

                new_fname = input("Enter new first name: ") or fname
                new_lname = input("Enter new last name: ") or lname
                new_phone = input("Enter new phone number: ") or phone_number
                new_email = input("Enter new email: ") or email

                content[i] = f"{new_fname}|{new_lname}|{new_phone}|{new_email}\n"
                updated = True
                break

        if updated:
            with open(filename, 'w') as file_object:
                file_object.writelines(content)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

# Main application
if __name__ == "__main__":
    os.system('clear')

    while True:
        print("*** Contact Book ***\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            os.system('clear')
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")

            contact = Contacts(fname, lname, phone_number, email)
            contact.store_names()
            print("\nContact saved successfully!")
            input("\nPress Enter to continue...")

        elif choice == '2':
            os.system('clear')
            Contacts.view_names()
            input("\nPress Enter to continue...")

        elif choice == '3':
            os.system('clear')
            target = input("Enter Phone Number to search: ")
            Contacts.search_names(target)
            input("\nPress Enter to continue...")

        elif choice == '4':
            os.system('clear')
            target = input("Enter Phone Number to update: ")
            Contacts.update_contacts(target)
            input("\nPress Enter to continue...")

        elif choice == '5':
            os.system('clear')
            target = input("Enter Phone Number to delete: ")
            Contacts.delete_contacts(target)
            input("\nPress Enter to continue...")

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please try again.")
            input("\nPress Enter to continue...")

        os.system('clear')
