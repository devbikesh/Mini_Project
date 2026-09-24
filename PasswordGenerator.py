import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

password_length = int(input("Enter password length: "))

password = ""

for _ in range(password_length):
    random_character = random.choice(characters)
    password += random_character

print("Your generated password:", password)



