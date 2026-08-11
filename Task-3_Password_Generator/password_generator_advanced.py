import tkinter as tk
import secrets
import string
import pyperclip
def generate_password():
    try:
        length = int(length_spinbox.get())
        if length < 8:
            result_label.config(
                text="Password length must be at least 8!",
                fg="red"
            )
            strength_label.config(text="")
            copy_label.config(text="")
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
            strength_label.config(text="")
            copy_label.config(text="")
            return
        characters = ""
        password_list = []
        if uppercase_var.get():
            characters += string.ascii_uppercase
            password_list.append(secrets.choice(string.ascii_uppercase))
        if lowercase_var.get():
            characters += string.ascii_lowercase
            password_list.append(secrets.choice(string.ascii_lowercase))
        if numbers_var.get():
            characters += string.digits
            password_list.append(secrets.choice(string.digits))
        if symbols_var.get():
            characters += string.punctuation
            password_list.append(secrets.choice(string.punctuation))
        while len(password_list) < length:
            if exclude_var.get():
                ambiguous = "0O1lI"
                characters = "".join(
                    c for c in characters
                    if c not in ambiguous
                )
                password_list = [
                    c for c in password_list
                    if c not in ambiguous
                ]
            password_list.append(secrets.choice(characters))
        secrets.SystemRandom().shuffle(password_list)
        password = "".join(password_list)
        history.insert(0, password)
        if len(history) > 5:
            history.pop()
        history_box.delete(0, tk.END)
        for pwd in history:
            history_box.insert(tk.END, pwd)
        pyperclip.copy(password)
        result_label.config(
            text=password,
            fg="green"
        )
        copy_label.config(
            text="✓ Password copied to clipboard!",
            fg="blue"
        )
        if length < 10 or selected == 2:
            strength = "Weak"
            color = "red"
        elif length < 14 or selected == 3:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Strong"
            color = "green"
        strength_label.config(
            text=f"Password Strength: {strength}",
            fg=color
        )
    except ValueError:
        result_label.config(
            text="Enter a valid password length!",
            fg="red"
        )
        strength_label.config(text="")
        copy_label.config(text="")
history = []
window = tk.Tk()
window.title("Advanced Password Generator")
window.geometry("500x450")
length_label = tk.Label(
    window,
    text="Password Length:"
)
length_label.pack(pady=5)
length_spinbox = tk.Spinbox(
    window,
    from_=8,
    to=50,
    width=10
)
length_spinbox.pack()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
exclude_var = tk.BooleanVar()
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
exclude_check = tk.Checkbutton(
    window,
    text="Exclude Ambiguous Characters (0 O 1 l I)",
    variable=exclude_var
)
exclude_check.pack()
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
strength_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold")
)
strength_label.pack(pady=5)
copy_label = tk.Label(
    window,
    text="",
    font=("Arial", 10)
)
copy_label.pack()
history_title = tk.Label(
    window,
    text="Last 5 Passwords"
)
history_title.pack(pady=(15, 5))
history_box = tk.Listbox(
    window,
    width=40,
    height=5
)
history_box.pack()
window.mainloop()