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
        """Stores users details"""   
        with open(filename, 'a') as file_object:
            file_object.write(f"{self.fname}|{self.lname}|{self.phone_number}|{self.email}\n")
    
    @staticmethod
    def view_names():
        """"displays all saved contacts"""

        if not os.path.exists(filename):
            print("No contacts found.")
            return

        with open(filename,'r') as file_object:
            content = file_object.readlines()

        if content:
            print("\t\t\t*** Saved Contacts ***\n")
            insertion_sort(content)          
            for line in content:
                fname, lname, phone_number, email = line.strip().split('|')
                print(f"Name: {fname} {lname}, Phone: {phone_number}, Email: {email}")

        else:
            print("No contacts found")

def insertion_sort(content):
    """sorting with insertion sort algorithm"""
    for i in range(1, len(content)):
        key = content[i]
        j = i - 1

        while j >= 0 and  content[j] > key:
            content[j + 1] = content[j]
            j -= 1
        content[j + 1] = key

if __name__ == "__main__":
    os.system('clear')

    while True:
        print("*** Contact Book ***\n")
        print("Enter the following details")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            os.system('clear')
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter Email: ")

            person = Contacts(fname, lname, phone_number, email)
            person.store_names()
            print("\n Contact saved successully!\n")

        elif choice == '2':
            os.system('clear')
            Contacts.view_names()
            input("\n Press Enter to continue...")

        elif choice == '3':
            print("Exiting Contact Book. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please try again")

        os.system('clear')
            




        

    