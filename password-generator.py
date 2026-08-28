# main task - have the program ask you the range of the password then output the result based on the answer. 
# the output needs to include uppercase and lowercase letters, numbers, and special characters regardless.
# the range will be 15 characters minimum. if the user asks for something lower or higher than 64 call it.
# if a letter or special character is entered, then call it.
import secrets
import string

def generate_password(length = 20):
    full_list = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(full_list) for i in range(length))
    return password

print("This is the Password Generator! ")
password = generate_password()
print(f"generated password: {password}")
# len = int(input("Enter a number for the length of the password:"))
# if len < 15:
#     print("This password length is too short.")
# elif len > 64:
#     print("This password is too long.")