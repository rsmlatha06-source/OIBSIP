import tkinter as tk
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            result_label.config(
                text="Password length must be at least 8!",
                fg="red"
            )
            return
        selected = (
                uppercase_var.get() +
                lowercase_var.get() +
                numbers_var.get() +
                symbols_var.get()
        )

        if selected < 2:
            result_label.config(
                text="Select at least 2 character types!",
                fg="red"
            )
            return
        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation
        password = ""
        for i in range(length):
            password += random.choice(characters)
        result_label.config(
            text=password,
            fg="green"
        )
    except ValueError:
        result_label.config(
            text="Enter a valid password length!",
            fg="red"
        )
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x400")
length_label = tk.Label(
    window,
    text="Password Length:"
)
length_label.pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(
    window,
    text="Include Uppercase (A-Z)",
    variable=uppercase_var
)
uppercase_check.pack()
lowercase_check = tk.Checkbutton(
    window,
    text="Include Lowercase (a-z)",
    variable=lowercase_var
)
lowercase_check.pack()
numbers_check = tk.Checkbutton(
    window,
    text="Include Numbers (0-9)",
    variable=numbers_var
)
numbers_check.pack()
symbols_check = tk.Checkbutton(
    window,
    text="Include Symbols (!@#$)",
    variable=symbols_var
)
symbols_check.pack()
generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=10)
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)
window.mainloop()