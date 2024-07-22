import string
import random

def password_generator(length):
    # Define the character set (uppercase, lowercase, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password =""
    for _ in range(length):
        password += random.choice(characters) 
    
    return password

def input_check(name):
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Generate the password of desired length
    password = password_generator(length)
    
    # Display the password on screen
    print("\n===================================================")
    print(f"{name}\nThis is your Generated Password : {password}")
    
    
print("\n\n==============Welcome to Password Generator==================\n")
name = input("Enter your name :")
input_check(name)

while True:
    more = input("\nwant to generate more password... :").lower()
    if more == "y" or more == "yes":
        input_check(name)
    else:
        print("\n========================================")
        print(f"Thanks {name} for using Password Generator")
        break
    
