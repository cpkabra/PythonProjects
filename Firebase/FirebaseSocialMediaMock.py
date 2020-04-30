
#@author Neel Patel
#@file FirebaseSocialMediaMock.py

import Firebase.BackendAndValidation as bv, sys
def validate_command(command):
    if command == "create new user" or command == "delete user" or command == "follow user" or command == "unfollow-user" or command == "print users" or command == "quit":
        return True
    return False

def intro():
    print()
    print("------------------------------------------------------------")
    print("|                FIREBASE SOCIAL MEDIA APP                 |")
    print("------------------------------------------------------------")
    print()
    print("----> Hello! Welcome to Command-Line Social Media App created")
    print("      with the help of Firebase.")
    print()
intro()
while True:
    print("Please select from the following commands below: ")
    print("-------------------------------------------------")
    print("create new user")
    print("delete user")
    print("follow user")
    print("unfollow-user")
    print("print users")
    print("quit")
    print()
    command = input("Please choose a command: ")
    while not validate_command(command):
        command = input("Please choose a valid command: ")
    if command == "quit":
        sys.exit()
    if command == "create new user":
        name = input("Please enter the full name: ")
        while " " not in name:
            name = input("Please enter the full name: ")
        email = input("Please enter the email address: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        bv.create_user(name,email)
    if command == "delete user":
        name = input("Please enter the full name: ")
        while " " not in name:
            name = input("Please enter the full name: ")
        email = input("Please enter the email address: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        bv.delete_user(name,email)
    if command == "follow user":
        name = input("Please enter the name of the user that wants to follow: ")
        while " " not in name:
            name = input("Please enter a valid full name: ")
        email = input("Please enter the email address of the user that wants to follow: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        follower_hashed = bv.get_hashed_user(name,email)
        name = input("Please enter the name of the user that wants to be follow: ")
        while " " not in name:
            name = input("Please enter a valid full name: ")
        email = input("Please enter the email address of the user that wants to be followed: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        following_hashed = bv.get_hashed_user(name,email)
        bv.follow(follower_hashed,following_hashed)
    if command == "unfollow-user":
        name = input("Please enter the name of the user that wants to un-follow: ")
        while " " not in name:
            name = input("Please enter a valid full name: ")
        email = input("Please enter the email address of the user that wants to un-follow: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        follower_hashed = bv.get_hashed_user(name, email)
        name = input("Please enter the name of the user that wants to be un-followed: ")
        while " " not in name:
            name = input("Please enter a valid full name: ")
        email = input("Please enter the email address of the user that wants to be un-followed: ")
        while "@" not in email or "." not in email:
            email = input("Please a valid email address: ")
        following_hashed = bv.get_hashed_user(name, email)
        bv.unfollow(follower_hashed, following_hashed)
    if command == "print users":
        bv.print_all_users()

