import random
import string
# generating a password in random way with characters, digits and punctuation
def generate_password(length):
    
    pass_char = string.ascii_letters + string.digits + string.punctuation #ascii_letters returns the characters.
    
    password = ""
    for _ in range(length):
        password += random.choice(pass_char) #random.choice taken the random values from pass_char variable.
    return password

def password():
    len = input("enter the length of the password: ")
    
    #  if the input is a positive number
    if len.isdigit() and int(len) > 0:  #len must be an integer and greater than zero
        length = int(len)
        password = generate_password(length)
        print(f"Generated password: {password}")
    else:
        print("Please enter a valid positive number.")

# Call the function to generate the password
password()
