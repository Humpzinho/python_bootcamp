from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Km to Miles Converter")
window.minsize(250, 100)
window.config(padx=20, pady=20)


def calculate():
    miles = float(input.get()) / 1.609
    label_miles_r.config(text=round(miles))


label_equals = Label(text='is equals to', font=("arial", 12))
label_equals.grid(column=0, row=2)

label_km = Label(text='km', font=("arial", 12))
label_km.grid(column=2, row=1)

label_miles = Label(text='miles', font=("arial", 12))
label_miles.grid(column=2, row=2)

label_miles_r = Label(text=0, font=("arial", 12))
label_miles_r.grid(column=1, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

input = Entry(width=10)
input.grid(column=1, row=1)

window.mainloop()
