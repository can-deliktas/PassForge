import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string
import pyperclip
import re
from datetime import datetime

# Password strength evaluation function
def evaluate_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "lowercase": bool(re.search(r"[a-z]", password)),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(rf"[{re.escape(string.punctuation)}]", password))
    }
    
    strength = sum(criteria.values())
    strength_levels = {
        5: ("Very Strong", "green"),
        4: ("Strong", "blue"),
        3: ("Medium", "orange"),
        2: ("Weak", "red"),
        1: ("Very Weak", "darkred"),
        0: ("Very Weak", "darkred")
    }
    return strength_levels.get(strength, ("Very Weak", "darkred"))

# Password generator function
def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_special_chars = special_chars_var.get()

        if length < 4:
            messagebox.showwarning("Invalid Input", "Password length should be at least 4 characters.")
            return

        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Selection Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
        
        strength_text, color = evaluate_password_strength(password)
        strength_label.config(text=f"Strength: {strength_text}", fg=color)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")

# Copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# Save password to a file
def save_password():
    password = password_var.get()
    if not password:
        messagebox.showwarning("No Password", "Generate a password first.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    default_filename = f"password_{timestamp}.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile=default_filename)
    
    if file_path:
        with open(file_path, "w") as f:
            strength_text, _ = evaluate_password_strength(password)
            f.write(f"Password: {password}\n")
            f.write(f"Strength: {strength_text}\n")
            f.write(f"Generated on: {timestamp}\n")
            f.write("\n---\nPassForge\n")
            f.write("https://github.com/can-deliktas/PassForge/\n")
            f.write("Contributors:\n")
            f.write("can-deliktas\n")
            f.write("DevByte1328\n")
        messagebox.showinfo("Saved", f"Password saved to: {file_path}")

# Clear fields
def clear_fields():
    password_var.set("")
    length_entry.delete(0, tk.END)
    strength_label.config(text="Strength:", fg="black")

# GUI setup
root = tk.Tk()
root.title("PassForge - Password Generator")
root.geometry("400x320")
root.resizable(False, False)

# Widgets
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Frame for checkboxes (brings them closer together)
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=2)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=False)

letters_check = tk.Checkbutton(checkbox_frame, text="Letters", variable=letters_var)
letters_check.pack(side=tk.LEFT, padx=2)

numbers_check = tk.Checkbutton(checkbox_frame, text="Numbers", variable=numbers_var)
numbers_check.pack(side=tk.LEFT, padx=2)

special_chars_check = tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_chars_var)
special_chars_check.pack(side=tk.LEFT, padx=2)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), justify="center", state="readonly")
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength:", font=("Arial", 10, "bold"))
strength_label.pack()

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear_fields)
clear_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=5)

# Run application
root.mainloop()
