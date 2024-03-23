from tkinter import *

# Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=15, pady=15)


def calculate():
    choice = degrees.get()
    result_text["text"] = int(choice) * 1.609


# Text
miles_text = Label(text="Miles", font=("Arial", 12))
equal_text = Label(text="is equal to", font=("Arial", 12))
result_text = Label(text="0", font=("Arial", 12))
km_text = Label(text="Km", font=("Arial", 12))

# Text Placements
miles_text.grid(row=0, column=3)
equal_text.grid(row=1, column=0)
result_text.grid(row=1, column=2)
km_text.grid(row=1, column=3)

# Input
degrees = Entry(width=10)
degrees.grid(row=0, column=2)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=2)

window.mainloop()
