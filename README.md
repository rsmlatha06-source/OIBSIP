# Advanced Password Generator

## Description

This is a Python GUI-based Advanced Password Generator developed using **Tkinter**. The application allows users to generate secure passwords based on selected criteria such as password length and character types. It uses Python's **secrets** module for cryptographically secure password generation and includes additional security features like password strength analysis, clipboard support, and password history.

---

## Features

### Beginner Features

- GUI built using Tkinter
- User can select password length
- Include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Symbols
- Minimum password length of 8 characters
- Requires at least two character types to be selected
- Generates a random password
- Handles invalid input using exception handling

---

### Advanced Features

- Uses **Spinbox** for password length selection
- Uses Python **secrets** module for secure password generation
- Guarantees at least one character from each selected character type
- Password Strength Indicator:
  - 🔴 Weak
  - 🟠 Medium
  - 🟢 Strong
- Automatically copies generated password to the clipboard using **pyperclip**
- Option to exclude ambiguous characters:
  - 0, O, 1, l, I
- Displays the last five generated passwords during the current session

---

## Technologies Used

- Python
- Tkinter
- Secrets
- String
- Pyperclip

---

## Project Files

```text
Task-3_Password_Generator/
│── password_generator.py
│── README.md
```

---

## How to Run

1. Open the project in PyCharm.
2. Install the required library:

```bash
pip install pyperclip
```

3. Run:

```text
password_generator.py
```

4. Select:
   - Password length
   - Character types
5. Click **Generate Password**.
6. The password will:
   - Be displayed on the screen
   - Be copied automatically to the clipboard
   - Show its strength
   - Be added to the last five passwords history

---

## Example

### Input

```text
Password Length: 12

✓ Uppercase
✓ Lowercase
✓ Numbers
✓ Symbols
✓ Exclude Ambiguous Characters
```

### Output

```text
Password:
9[+2D7vSsT]P

Password Strength:
Medium

✓ Password copied to clipboard!
```

---

## Future Improvements

- Save password history to an encrypted file
- Export passwords to PDF
- Generate QR codes for passwords
- Dark mode interface
- Custom symbol selection
- Password expiration reminder

---

## Author

Developed as part of the **Oasis Infobyte Python Programming Internship (OIBSIP)**.
