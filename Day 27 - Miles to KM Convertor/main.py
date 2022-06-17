from tkinter import *


def calculate_press():
    miles_value = int(miles_input.get())
    km_output.config(text=int(miles_value * 1.609))


window = Tk()
window.config(padx=20, pady=20)
window.minsize(width=300, height=200)
window.title("Miles to KM Converter")

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1, padx=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=30)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1, padx=30)

calculate = Button(text="Calculate", command=calculate_press)
calculate.grid(column=1, row=2, pady=30)

window.mainloop()
