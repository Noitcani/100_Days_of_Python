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
work_counter = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps, work_counter
    reps = 0
    work_counter = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_time, text="25:00")
    window.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    checkmark.config(bg=YELLOW)
    timer_label.config(bg=YELLOW, fg=GREEN, text="Timer")
    checkmark.config(bg=YELLOW, fg=GREEN, text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, work_counter
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        count_down(long_break)
        window.config(bg=RED)
        canvas.config(bg=RED)
        checkmark.config(bg=RED)
        timer_label.config(bg=RED, fg=YELLOW, text="Break")
        checkmark.config(bg=RED, fg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break)
        window.config(bg=PINK)
        canvas.config(bg=PINK)
        checkmark.config(bg=PINK)
        timer_label.config(bg=PINK, fg=YELLOW, text="Break")
        checkmark.config(bg=PINK, fg=YELLOW)

    else:
        count_down(work_sec)
        window.config(bg=GREEN)
        canvas.config(bg=GREEN)
        checkmark.config(bg=GREEN)
        timer_label.config(bg=GREEN, fg=YELLOW, text="Work!")
        checkmark.config(bg=GREEN, fg=YELLOW)
        work_counter += 1
        if work_counter < 5:
            checkmark.config(text="✓ " * work_counter)
        else:
            work_counter = 1
            checkmark.config(text="✓ " * work_counter)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(time_amount):

    count_min = time_amount // 60
    count_sec = time_amount % 60
    canvas.itemconfig(canvas_time, text=f"{count_min:02d}:{count_sec:02d}")
    global timer
    if time_amount > 0:
        timer = window.after(1000, count_down, time_amount - 1)
    else:
        window.attributes("-topmost", 1)
        window.deiconify()
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=YELLOW)

timer_label = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1, pady=10)

start_button = Button(text="Start", width=8, bg="white", bd=1, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=8, bg="white", bd=1, command=reset)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
checkmark.grid(column=1, row=3)


window.mainloop()