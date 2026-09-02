# main task - have the program ask you the range of the password then output the result based on the answer. 
# the output needs to include uppercase and lowercase letters, numbers, and special characters regardless.
# the range will be 15 characters minimum. if the user asks for something lower or higher than 64 call it.
# if a letter or special character is entered, then call it.
import secrets
import string

print("This is the Password Generator! ")

def generate_password(length = 25):
    length = int(input("Enter the length of your password: "))
    if length <= 14:
        print("This password is too short.")
        return
    elif length >= 65:
        print("This password is too long.")
        return

    full_list = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(full_list) for i in range(length))
    return password


password = generate_password()
print(f"generated password: {password}")
