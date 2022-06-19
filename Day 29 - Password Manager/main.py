from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_gen():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list.extend([random.choice(letters) for a in range(random.randint(8, 10))])
    password_list.extend([random.choice(symbols) for b in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for c in range(random.randint(2, 4))])

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showwarning(title="Missing Info",
                               message="Website, Username or Password cannot be empty")

    else:
        confirm_dialog = messagebox.askokcancel(title=website_input.get(),
                                                message=f"These are the details entered:\n\n "
                                                        f"Username: {email_input.get()}\n"
                                                        f"Password: {password_input.get()}")

        if confirm_dialog:
            with open("pw_data.txt", mode="a") as f:
                f.write(f"\n{website_input.get()}  |  {email_input.get()}  |  {password_input.get()}")
                website_input.delete(0, END)
                email_input.delete(0, END)
                email_input.insert(END, "your_email@email.com")
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

logo = PhotoImage(file="logo.png")

canvas = Canvas()
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=55)
website_input.grid(sticky="w", column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=55)
email_input.insert(END, "your_email@email.com")
email_input.grid(sticky="w", column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.config(width=35)
password_input.grid(sticky="w", column=1, row=3)

generate_pw_button = Button(text="Generate Password", command=pw_gen)
generate_pw_button.grid(sticky="w", column=2, row=3, padx=10)

add_button = Button(text="Add", command=add_pw)
add_button.config(width=46)
add_button.grid(sticky="w", column=1, row=4, columnspan=2)

window.mainloop()
