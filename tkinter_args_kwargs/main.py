# def add(*val):
#     result = 0
#     for n in val:
#         result = result + n
#     return result

# vals = input("add values (seperate with blank space): ")
# vals_list = [float(val) for val in vals.split()]
# print(vals_list)
# add(1,2,3,4,5)

from tkinter import *


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label.config(text=entry.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

entry = Entry(width=15)
entry.pack()
print(entry.get())

window.mainloop()
