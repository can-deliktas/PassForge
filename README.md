# PassForge - Password Generator & Strength Evaluator

PassForge is a powerful and customizable password generator and strength evaluator tool written in Python. It allows users to generate strong passwords with various options, evaluate the strength of the generated passwords, and save them securely. Additionally, passwords can be copied to the clipboard for convenience.

---

## 🛠️ **Features**

- **Customizable Password Generation**:  
  Generate passwords with customizable length, and include letters, numbers, and special characters.
  
- **Password Strength Evaluation**:  
  Evaluate password strength based on length and character variety (Weak, Moderate, Strong).

- **Clipboard Support**:  
  Easily copy the generated password to the clipboard with one click.

- **Save Password to File**:  
  Optionally save the password to a text file, including the password itself, generation date, and strength evaluation.

- **Terminal User Interface**:  
  A simple, interactive, and colorful terminal-based user interface.

---

## 📥 **Installation & Setup**

To get started with PassForge, follow the steps below:

### 1️⃣ **Clone the Repository**

First, clone the repository to your local machine using the following command:

```
git clone https://github.com/can-deliktas/PassForge.git
cd PassForge
```

### 2️⃣ **Install Dependencies**

This project requires Python 3+ along with a few external libraries. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

### 3️⃣ **Run the Program**

Once the dependencies are installed, you can run the program with:

```
python3 PassForge.py
```

---

## 🎯 **Usage**

When you launch the program, you will be presented with the following options:

```
=== PassForge ===
1. Generate Password
2. Exit
```

1. **Generate Password**:  
   This option allows you to create a password by specifying the desired length and character types (letters, numbers, special characters). After the password is generated, you will be prompted with the following options:
   - **Copy to Clipboard**: Choose to copy the password to your clipboard.
   - **Save to File**: Choose to save the password in a text file with a timestamp and password strength evaluation.

2. **Exit**:  
   Exits the program gracefully.

---

## 📄 **Generated Password Format**

When you choose to save the password to a file, the content of the file will look like this:

```
Password: w4Y#p2B7Z$W
Generated on: 2025-02-20_14-30-00
Password Strength: Strong
Signature: PassForge
```

The password, generation timestamp, strength evaluation, and the signature ("PassForge") are written to the file.

---

## 💡 **Password Strength Evaluation**

The password strength is evaluated based on the following criteria:
- **Weak**: Short password (less than 8 characters).
- **Moderate**: Moderate length (8–12 characters).
- **Strong**: Strong password (12+ characters).

The password strength will be printed on the screen and saved along with the password in the output file.

---

## 🗂️ **Project Structure**

The project directory structure is as follows:

```
PassForge/
│── PassForge.py                # Main program file containing the logic
│── README.md                   # Project documentation
│── requirements.txt            # List of dependencies for the project
│── LICENSE                     # License file
```

---

## 📝 **License and Copyright**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
© 2025 can-deliktas 
---

## 🤝 **Contributing**

Contributions are welcome! If you would like to contribute to PassForge, follow these steps:

### 1️⃣ **Fork the Repository**

Click the "Fork" button on the top-right of the repository to make a copy of this repository under your GitHub account.

### 2️⃣ **Create a New Branch**

To create a new branch for your feature or fix, use the following command:

```
git checkout -b new-feature
```

### 3️⃣ **Make Changes**

Edit the code or documentation to add new features or fix bugs.

### 4️⃣ **Commit Your Changes**

Once you are satisfied with the changes, commit them:

```
git add .
git commit -m "Added new feature"
```

### 5️⃣ **Push Changes**

Push the changes to your forked repository:

```
git push origin new-feature
```

### 6️⃣ **Submit a Pull Request**

Go to the original repository and open a pull request to merge your changes. 

We’ll review your changes and if everything looks good, we’ll merge it into the main project.

---

## 📚 **Acknowledgements**

- This project uses several open-source libraries to enhance functionality:
  - `pyperclip`: For copying passwords to the clipboard.
  - `termcolor`: To make the terminal output colorful and interactive.
  - `random`, `string`: For generating random passwords with various character sets.

---

## 👨‍💻 **Developer Notes**

PassForge was designed to be simple yet powerful. It focuses on providing customizable password generation, real-time password strength evaluation, and convenient file-saving features. The code is modular, allowing for easy enhancements and improvements.

### Future Enhancements
- **Graphical User Interface (GUI)**: Implement a GUI using `Tkinter` or other libraries to make it more user-friendly.
- **Password History**: Store and retrieve previously generated passwords securely.
- **Additional Password Strength Metrics**: Include more complex password strength evaluation, such as entropy or advanced algorithms.
  
We welcome all suggestions and contributions to improve PassForge!

---

PassForge – **Secure Your Passwords with Ease** 🔐

```
