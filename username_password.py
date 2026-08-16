#validate user input exeercise
# 1. not less than 8 characters long
# 2. must not contain spaces
# 3. must not contain digits

import getpass


username = input("Enter your username: ")
while len(username) < 8:
    print("username must be at least 8 characters long")
    username = input("enter your username: ")
while " " in username:
    print("username must not contain spaces")
    username = input("enter your username: ")
while any(char.isdigit() for char in username) and any(char.isalpha() for char in username):
    print("username must not contain both digits and letters")
    username = input("enter your username: ")
while any(char.isdigit() for char in username):
    print("username must not contain digits")
    username = input("enter your username: ")
print("username is valid")

#1.passsword must be at least 7 characters long.
#2.passwoord must contain at least one digit.
#3.special characters are allowed but not required.
#4.password must contain at least one uppercase letter.
#5.password must match the confirmation password.


password = getpass.getpass("Enter your password: ")
while len(password) < 7:
    print("password must be at least 7 characters long")
    password = getpass.getpass("Enter your password: ")
while not any(char.isdigit() for char in password):
    print("password must contain at least one digit")
    password = getpass.getpass("Enter your password: ")
while not any(char.isupper() for char in password):
    print("password must contain at least one uppercase letter")
    password = getpass.getpass("Enter your password: ")
else:
    confirm_password = input("Confirm your password: ")
    while confirm_password != password:
        print("passwords do not match")
        confirm_password = input("Confirm your password: ")
    else:
        if confirm_password == password:
            print("passwords match!")
