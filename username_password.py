# Validate user input exercise
# Username rules:
# 1. At least 8 characters long
# 2. Must not contain spaces
# 3. Must not contain digits
#
# Password rules:
# 1. At least 7 characters long
# 2. Must contain at least one digit
# 3. Special characters are allowed but not required
# 4. Must contain at least one uppercase letter
# 5. Must match the confirmation password

import getpass


def validate_username(username: str) -> tuple[bool, str]:
    if len(username) < 8:
        return False, "Username must be at least 8 characters long"
    if " " in username:
        return False, "Username must not contain spaces"
    if any(char.isdigit() for char in username):
        return False, "Username must not contain digits"
    return True, "Username is valid"


def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 7:
        return False, "Password must be at least 7 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    return True, "Password is valid"


# Username section
while True:
    username = input("Enter your username: ")
    is_valid, message = validate_username(username)
    print(message)
    if is_valid:
        break

# Password section
while True:
    password = getpass.getpass("Enter your password: ")
    is_valid, message = validate_password(password)
    print(message)
    if is_valid:
        break

# Confirm password
while True:
    confirm = getpass.getpass("Confirm your password: ")
    if confirm == password:
        print("Passwords match!")
        break
    print("Passwords do not match")
