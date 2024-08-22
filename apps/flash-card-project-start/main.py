from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA SETUP ------------------------------- #
try:
    words_data = pd.read_csv("data/words_to_remember.csv")
except FileNotFoundError:
    words_data = pd.read_csv("data/french_words.csv")
    words_data.to_csv("data/words_to_remember.csv", index=False)

# print(words_data["French"])
words_data_dict = words_data.to_dict(orient="records")
temp_words_data_dict = words_data_dict.copy()
# print(words_data_dict)
current_word = ""


def right():
    global current_word
    if current_word != "" and current_word in temp_words_data_dict:
        print(current_word)
        temp_words_data_dict.remove(current_word)
        save_data = pd.DataFrame(temp_words_data_dict)
        save_data.to_csv("data/words_to_remember.csv", index=False)
    new_word()


def wrong():
    global current_word
    if current_word != "" and current_word not in temp_words_data_dict:
        print(current_word)
        temp_words_data_dict.append(current_word)
        save_data = pd.DataFrame(temp_words_data_dict)
        save_data.to_csv("data/words_to_remember.csv", index=False)
    new_word()


# ---------------------------- NEW WORD ------------------------------- #
def new_word():
    global count_task_id, current_word
    if count_task_id !=0:
        window.after_cancel(count_task_id)
    
    # current_word = words_data["French"].sample().values[0]
    current_word = random.choice(words_data_dict)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="#000000")
    canvas.itemconfig(word_text, text=current_word["French"], fill="#000000")
    count(3)


# ---------------------------- CHANGE TO ENGLISH ------------------------------- #
def show_english():
    global current_word
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="#FFFFFF")
    canvas.itemconfig(word_text, text=current_word["English"], fill="#FFFFFF")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #     
count_task_id = 0
def count(seconds):
    global count_task_id
    if seconds > 0:
        count_task_id = window.after(1000, count, seconds - 1)
    else:
        show_english()


# ---------------------------- GUI SETUP ------------------------------- # 
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(1000)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
canvas.create_image(400, 263, image=card_back_img)
card_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"),)
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, bd=0, command=right)
right_button.grid(row=1, column=1)

new_word()

window.mainloop()