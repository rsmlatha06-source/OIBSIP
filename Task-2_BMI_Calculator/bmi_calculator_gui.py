import matplotlib.pyplot as plt
import tkinter as tk
import csv
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("450x400")
def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            result_label.config(
                text="Weight and height must be greater than 0.",
                fg="red"
            )
            return
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        result_label.config(
            text=f"Your BMI is: {bmi:.2f}\nCategory: {category}",
            fg=color
        )
        with open("bmi_records.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, weight, height, round(bmi, 2), category])
    except ValueError:
        result_label.config(
            text="Please enter valid numbers.",
            fg="red"
        )
def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("500x300")
    text = tk.Text(history_window, width=60, height=15)
    text.pack()
    try:
        with open("bmi_records.csv", "r") as file:
            reader = csv.reader(file)

            text.insert(
                tk.END,
                "Name\tWeight\tHeight\tBMI\tCategory\n"
            )
            text.insert(
                tk.END,
                "-" * 50 + "\n"
            )
            for row in reader:
                text.insert(
                    tk.END,
                    f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n"
                )
    except FileNotFoundError:
        text.insert(tk.END, "No BMI records found.")
def show_graph():

    names = []
    bmi_values = []

    try:
        with open("bmi_records.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                names.append(row[0])
                bmi_values.append(float(row[3]))

        plt.figure(figsize=(8,5))
        plt.plot(names, bmi_values, marker="o")

        plt.title("BMI Trend")
        plt.xlabel("Name")
        plt.ylabel("BMI")

        plt.grid(True)

        plt.show()

    except FileNotFoundError:
        result_label.config(
            text="No BMI records found.",
            fg="red"
        )
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()
height_label = tk.Label(window, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()
calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi
)
calculate_button.pack(pady=10)
history_button = tk.Button(
    window,
    text="Show History",
    command=show_history
)
history_button.pack()
graph_button = tk.Button(
    window,
    text="Show BMI Graph",
    command=show_graph
)
graph_button.pack(pady=5)
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)
window.mainloop()