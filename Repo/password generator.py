import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return ""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number")

print("             PASSWORD GENERATOR              ")
main()