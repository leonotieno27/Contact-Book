"""Contact books"""

import os
import sys

filename = 'contacts.txt'

class Contacts:
    def __init__(self, fname, lname, number, email):
        """initializing attributes"""
        self.fname = fname
        self.lname = lname
        self.phone_number = number
        self.email = email

    def store_names(self):
        """Stores user's details"""
        with open(filename, 'a') as file_object:
            file_object.write(f"{self.fname}|{self.lname}|{self.phone_number}|{self.email}\n")

    @staticmethod
    def search_names(target):
        """Searches contacts by phone number using binary search"""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        if not content:
            print("No contacts found.")
            return

        # Sort the content by phone number for binary search
        content.sort(key=lambda line: line.split('|')[2])  # Sort by phone number

        # Perform binary search
        left, right = 0, len(content) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_phone = content[mid].split('|')[2]  # Extract phone number

            if mid_phone == target:
                # Contact found
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

        # Contact not found
        print("Contact not found.")

    @staticmethod
    def view_names():
        """Displays all saved contacts"""
        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename, 'r') as file_object:
            content = file_object.readlines()

        if content:
            print("\t\t\t*** Saved Contacts ***\n")
            insertion_sort(content)          
            for line in content:
                fname, lname, phone_number, email = line.strip().split('|')
                print(f"Name: {fname} {lname}, Phone: {phone_number}, Email: {email}")
        else:
            print("No contacts found.")

def insertion_sort(content):
    """Sorting with insertion sort algorithm"""
    for i in range(1, len(content)):
        key = content[i]
        j = i - 1

        while j >= 0 and content[j] > key:
            content[j + 1] = content[j]
            j -= 1
        content[j + 1] = key

if __name__ == "__main__":
    os.system('clear')

    while True:
        print("*** Contact Book ***\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            os.system('clear')
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter Email: ")

            person = Contacts(fname, lname, phone_number, email)
            person.store_names()
            print("\nContact saved successfully!\n")
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
            print("Exiting Contact Book. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please try again.")

        os.system('clear')
