
import random
import string
import pyperclip
import termcolor
from termcolor import cprint
import os
import time
from datetime import datetime
from terminal_graphics import *
import re

# Password strength evaluation function
def evaluate_password_strength(password):
    """
    Evaluates the strength of the password based on the following criteria:
    1. Length of the password
    2. Contains at least one lowercase letter
    3. Contains at least one uppercase letter
    4. Contains at least one digit
    5. Contains at least one special character

    Args:
    - password (str): The password to evaluate.

    Returns:
    - str: The strength of the password ("Very Weak", "Weak", "Medium", "Strong", "Very Strong").
    """
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!#$%&@€₺]", password):
        strength += 1

    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Password generator function
def generate_password(length, use_letters, use_numbers, use_special_chars):
    """
    Generates a password based on the selected length and criteria.

    Args:
    - length (int): Length of the password.
    - use_letters (bool): Whether to include letters in the password.
    - use_numbers (bool): Whether to include numbers in the password.
    - use_special_chars (bool): Whether to include special characters in the password.

    Returns:
    - str: The generated password.
    """
    characters = ""

    if use_letters:
        characters += string.ascii_letters  # Lowercase + Uppercase letters
    if use_numbers:
        characters += string.digits  # Digits
    if use_special_chars:
        characters += "!#$%&@€₺"  # Special characters

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print(termcolor.colored("Password copied to clipboard!", "green"))

# Save password and its strength to a file
def save_password(password, strength):
    save_choice = input("Do you want to save the password to a file? (y/n): ").lower()
    if save_choice == "y":
        # Create a filename with the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        save_path = f"password_{timestamp}.txt"  # For example: password_2025-xx-xx_17-30-00.txt
        with open(save_path, 'w') as f:
            # Save password, strength, and timestamp
            f.write(f"Password: {password}\n")
            f.write(f"Strength: {strength}\n")
            f.write(f"Generated on: {timestamp}\n")
            f.write("\n---\nPassForge\n")
            f.write("https://github.com/can-deliktas/PassForge/\n")
            f.write("Contributors:\n")
            f.write("can-deliktas\n")

        print(f"Password saved to: {save_path}")
    else:
        print("Password was not saved.")

# Display menu
def display_menu():
    # Main menu
    cprint("Welcome to PassForge", "cyan", attrs=["bold"])
    cprint("1. Generate Password", "yellow")
    cprint("2. Exit", "red")

# Get user selection
def get_user_option():
    option = input("Select an option: ")
    return option

# Get user input for password generation
def get_user_input():
    length = int(input("Enter password length: "))
    use_letters = input("Include letters (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters (y/n): ").lower() == 'y'
    return length, use_letters, use_numbers, use_special_chars

# Main function
def main():
    while True:
        # Show the main menu
        display_menu()
        option = get_user_option()

        if option == "1":
            # Get user input for password options
            length, use_letters, use_numbers, use_special_chars = get_user_input()
            
            # Generate the password
            password = generate_password(length, use_letters, use_numbers, use_special_chars)

            # Show the generated password and evaluate its strength
            print(f"Generated password: {termcolor.colored(password, 'yellow')}")
            strength = evaluate_password_strength(password)
            print(f"Password Strength: {termcolor.colored(strength, 'green')}")

            # Ask if user wants to copy password to clipboard
            copy_choice = input("Do you want to copy the password to clipboard? (y/n): ").lower()
            if copy_choice == "y":
                copy_to_clipboard(password)

            # Ask if user wants to save the password
            save_password(password, strength)

        elif option == "2":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
