# BMI Calculator

## Description

This is a Python GUI-based BMI (Body Mass Index) Calculator developed using Tkinter. The application calculates a user's BMI based on weight and height, displays the BMI category with color-coded results, saves records to a CSV file, shows BMI history, and plots a BMI trend graph.

---

## Features

- GUI built using Tkinter
- Accepts user's name, weight (kg), and height (m)
- Calculates BMI using the standard formula
- Displays BMI rounded to 2 decimal places
- Classifies BMI into:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Color-coded BMI result:
  - 🔵 Blue = Underweight
  - 🟢 Green = Normal
  - 🟠 Orange = Overweight
  - 🔴 Red = Obese
- Saves BMI records to a CSV file
- Displays BMI history
- Shows a BMI comparison graph using Matplotlib.
- Handles invalid input using exception handling
- Prevents zero and negative values

---

## Formula

```text
BMI = Weight / (Height × Height)
```

---

## Technologies Used

- Python
- Tkinter
- CSV
- Matplotlib

---

## Project Files

```text
Task-2_BMI_Calculator/
│── bmi_calculator.py          # Console version
│── bmi_calculator_gui.py      # GUI version
│── README.md
```

---

## How to Run

1. Open the project in PyCharm.
2. Run `bmi_calculator_gui.py`.
3. Enter:
   - Name
   - Weight (kg)
   - Height (m)
4. Click **Calculate BMI**.
5. View your BMI and category.
6. Click **Show History** to view previous records.
7. Click **Show BMI Graph** to display the BMI trend graph.

---

## Example

### Input

```text
Name: Madhu
Weight: 60
Height: 1.65
```

### Output

```text
Your BMI is: 22.04
Category: Normal
```

---

## Future Improvements

- Delete BMI records
- Search records by name
- Export records to Excel
- Display charts with different styles
- Add date and time for each BMI record

---

## Author

Developed as part of the **Oasis Infobyte Python Programming Internship (OIBSIP)**.
