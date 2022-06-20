import pandas
from tkinter import *
from tkinter import messagebox
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")

data_list = data.to_dict(orient="records")
current_card = None


# ------------------------------Gen Next Word (Correct & Wrong)------------------------------------#
def next_word():
    window.after_cancel(count_down)
    global current_card
    try:
        current_card = choice(data_list)
    except IndexError:
        messagebox.showinfo(title="Learning Complete", message="Learning Complete!\nNo more words to learn!")
        quit()

    # Display French word
    card_canvas.itemconfig(language_label, text="French", fill="black")
    card_canvas.itemconfig(word_shown, text=current_card["French"], fill="black")
    card_canvas.itemconfig(card_pic, image=card_front)

    # Countdown and flip card
    flip_card(3)


def next_word_correct():
    data_list.remove(current_card)
    df = pandas.DataFrame(data_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# ------------------------------Timer------------------------------------#
def flip_card(time_left):
    global count_down
    if time_left > 0:
        time_left -= 1
        count_down = window.after(1000, flip_card, time_left)
        card_canvas.itemconfig(ticker, text=time_left)

    else:
        card_canvas.itemconfig(card_pic, image=card_back)
        card_canvas.itemconfig(language_label, text="English", fill="white")
        card_canvas.itemconfig(word_shown, text=current_card["English"], fill="white")
        card_canvas.itemconfig(ticker, text="")


# ------------------------------UI Setup------------------------------------#
# Set up Window
window = Tk()
window.title("Flash Cards App")
window.minsize(width=940, height=750)
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (940 / 2)
y = ((hs / 2) - (700 / 2) - 60)
window.geometry('%dx%d+%d+%d' % (940, 700, x, y))
count_down = window.after(1000, flip_card, 3)

# Import images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_tick = PhotoImage(file="images/right.png")
wrong_cross = PhotoImage(file="images/wrong.png")

# Card Canvas
card_canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_pic = card_canvas.create_image(450, 300, image=card_front)
# Labels
language_label = card_canvas.create_text(450, 150, text="", font=("Ariel", 30, "italic"))
word_shown = card_canvas.create_text(450, 300, text="", font=("Ariel", 60, "bold"))
ticker = card_canvas.create_text(780, 80, text="3", font=("Ariel", 30, "bold"), fill="brown")

card_canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = Button(image=right_tick, highlightthickness=0, command=next_word_correct)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_cross, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

next_word()
window.mainloop()
