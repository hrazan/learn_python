from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
task_id = 0
is_running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps, task_id, is_running
    window.after_cancel(task_id)
    reps = 0
    is_running = False
    title_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global is_running
    if not is_running:
        is_running = True
        title_label.config(text="WORK TIME", fg=GREEN)
        # count_down(60 * WORK_MIN)
        count_down(5)

def timer_continue():
    global reps, task_id, is_running
    if reps==0 or reps==2 or reps==4 or reps==6:
        title_label.config(text="WORK TIME", fg=GREEN)
        # count_down(60 * WORK_MIN)
        count_down(5)
    elif reps==1 or reps==3 or reps==5:
        title_label.config(text="SHORT BREAK TIME", fg=PINK)
        # count_down(60 * SHORT_BREAK_MIN)
        count_down(3)
    elif reps==7:
        title_label.config(text="LONG BREAK TIME", fg=RED)
        # count_down(60 * LONG_BREAK_MIN)
        count_down(4)
    else:
        timer_reset()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #     
def count_down(count):
    global reps, task_id
    check = ""
    for n in range((reps+1)//2):
        check += "✔"
    check_label.config(text=check)
    if count >= 0:
        minutes = count//60
        seconds = count%60

        if minutes < 10:
            minutes = f"0{minutes}"
        else:
            minutes = f"{minutes}"

        if seconds < 10:
            seconds = f"0{seconds}"
        else:
            seconds = f"{seconds}"

        canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
        task_id = window.after(1000, count_down, count - 1)
        print(task_id)
    else:
        # window.after_cancel(task_id)
        reps += 1
        timer_continue()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
check_label.grid(column=1, row=3)

window.mainloop()