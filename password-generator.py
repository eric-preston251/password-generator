# main task - have the program ask you the range of the password then output the result based on the answer. 
# the output needs to include uppercase and lowercase letters, numbers, and special characters regardless.
# the range will be 15 characters minimum. if the user asks for something lower or higher call it.
# if a letter or special character is entered, then call it.

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '`~!@#$%^&*()-_=+][}{\|;:,<.>/?'

all_chars = lowercase + uppercase + numbers + special

print("This is the Password Generator! Enter a number for the length of the password:")
password_length = input()
print(f"New Password: {password_length}")