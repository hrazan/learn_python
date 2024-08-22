from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

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
    website_entry_data = website_entry.get()
    email_entry_data = email_entry.get()
    password_entry_data = password_entry.get()

    if website_entry_data and email_entry_data and password_entry_data:
        is_to_save = False
        is_to_overwrite = False
        
        input_data_dict = {
            website_entry_data: {
                "email" : email_entry_data,
                "password" : password_entry_data,
            }
        }

        try:
            with open("save_data.json", mode="r") as file:
                file_data_dict = json.load(file)
                file.close()
        except FileNotFoundError:
            is_to_save = True
            file_data_dict = {}
            pass
        else:
            if website_entry_data in file_data_dict:
                prev_email = file_data_dict[website_entry_data]["email"]
                prev_password = file_data_dict[website_entry_data]["password"]
                is_ok = messagebox.askokcancel(title="Confirmation", message=
                                                   f"The following data:\n"
                                                   f"> Website: {website_entry_data}\n"
                                                   f"> Email/Username: {prev_email}\n"
                                                   f"> Password: {prev_password}\n"
                                                   f"will be overwrited with:\n"
                                                   f"> Website: {website_entry_data}\n"
                                                   f"> Email/Username: {email_entry_data}\n"
                                                   f"> Password: {password_entry_data}\n"
                                                   f"OK?")
                is_to_save = is_ok
            else:
                is_ok = messagebox.askokcancel(title="Confirmation" , message=
                                               f"The following data will be saved:\n"
                                               f"> Website: {website_entry_data}\n"
                                               f"> Email/Username: {email_entry_data}\n"
                                               f"> Password: {password_entry_data}\n"
                                               f"OK?")
                is_to_save = is_ok
        finally:
            if is_to_save:
                file_data_dict.update(input_data_dict)
                with open("save_data.json", mode="w") as file:
                    json.dump(file_data_dict, file, indent=4)
                    file.close()
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="ERROR", message="Please fill in all the data!")

# ---------------------------- SEARCH WEBSITE DATA ------------------------------- #
def search_website_data():
    website_name = website_entry.get()
    try:
        with open("save_data.json", mode="r") as file:
            file_data_dict = json.load(file)
            file.close()
    except FileNotFoundError:
        pass
    else:
        if website_name in file_data_dict:
            email_data = file_data_dict[website_name]["email"]
            password_data = file_data_dict[website_name]["password"]
            messagebox.showinfo(title="Search", message=
                                f"Data found:\n"
                                f"> Website: {website_name}\n"
                                f"> Email/Username: {email_data}\n"
                                f"> Password: {password_data}\n")
            return
    
    messagebox.showinfo(title="Search", message=f"Data for {website_name} not found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)

website_search_button = Button(text="Search", width=15, highlightthickness=0, command=search_website_data)
website_search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", width=15, highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, highlightthickness=0, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()