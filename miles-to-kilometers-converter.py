from tkinter import *


def calculate_km():
    miles = float(miles_input.get())
    # miles * 1.609344
    km = round(miles * 1.609)
    label_answer.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=120, pady=50)

# Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

# Is Equal to label
is_equal_label = Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=20, pady=20)

# Final answer display
label_answer = Label(text=0, font=("Arial", 14))
label_answer.grid(column=1, row=1)
label_answer.config(padx=20, pady=20)

# Kilometer label
kilometer_label = Label(text="Km", font=("Arial", 14))
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=20, pady=20)

# Calculate Button
button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()
