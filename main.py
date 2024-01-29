
from management import *

while True:
    print("\nContact Book Management System")
    print("Select 1 to Add Contactt")
    print("Select 2 to View Contact")
    print("Select 3 to Update Contact")
    print("Select 4 to Delete Contact")
    print("Select 5 to Exit")

    user_choice = input("Enter your option: ")

    #checking user option
    if user_choice == '1':
        add_contact()
    elif user_choice == '2':
        view_contacts()
    elif user_choice == '3':
        update_contact()
    elif user_choice == '4':
        delete_contact()
    else:
        exit_program()