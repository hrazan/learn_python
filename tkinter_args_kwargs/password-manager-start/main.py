from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password_list = [random.choice(string.ascii_letters) for i in range(8)] + [random.choice(string.digits) for i in range(2)] + [random.choice(string.punctuation) for i in range(2)]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    if website_entry.get() and email_entry.get() and password_entry.get():
        save = False
        data = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}"
        with open("save_data.txt", mode="r") as file:
            file_data = file.readlines()
            # print(data)
            # print(file_data)
            if data not in [_data.strip() for _data in file_data]:
                is_ok = messagebox.askokcancel(title="Confirmation" , message=f"The following data will be saved:\nWebsite: {website_entry.get()}\nEmail/Username: {email_entry.get()}\nPassword: {password_entry.get()}\nOK?")
                save = is_ok
            else:
                messagebox.showinfo(title="Info", message="This data has already been added.")
            file.close()

        if save:
            with open("save_data.txt", mode="a") as file:
                file.write(data + '\n')
                file.close()
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="ERROR", message="Please fill in all the data!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()