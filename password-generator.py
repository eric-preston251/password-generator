import secrets
import string

print("This is the Password Generator! ")

# Main method
def generate_password(length: int = 25):
    # Catches entered letters and special characters for input.
    try:
        length = int(input("Enter the length of your password (15-64): "))
    except ValueError:
        print("You entered either a letter or special character. Please enter a number between 15 and 64.")
        return
    # Accounts for input length based on the entered integer.
    if length <= 14:
        print("This password is too short.")
        return
    elif length >= 65:
        print("This password is too long.")
        return

    # Uses the imported libraries to call methods that compile all characters 
    # Loops through the list to securely choose characters based on user input.
    full_list = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(full_list) for i in range(length))
    return password

# Prints output
password = generate_password()
print(f"Generated password: {password}")
