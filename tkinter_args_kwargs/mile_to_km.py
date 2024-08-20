from tkinter import *


window = Tk()
# window.minsize(width=200, height=100)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label0 = Label(text="is equal to")
km_label0.grid(column=0, row=1)

km_label1 = Label(text="0")
km_label1.grid(column=1, row=1)

km_label2 = Label(text="Km")
km_label2.grid(column=2, row=1)

def miles_to_km():
    km_label1.config(text=str(float(miles_entry.get()) * 1.609344))

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()