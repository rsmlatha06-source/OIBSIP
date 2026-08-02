import tkinter as tk
import csv
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
def calculate_bmi():
    try:
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
            writer.writerow([weight, height, round(bmi, 2), category])
    except ValueError:
        result_label.config(
            text="Please enter valid numbers.",
            fg="red"
        )
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
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()
window.mainloop()