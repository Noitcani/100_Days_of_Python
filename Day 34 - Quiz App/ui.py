from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.config(height=550, width=340, pady=20, padx=20, bg=THEME_COLOR)
        self.window.minsize(height=450, width=340)
        self.score = 0
        self.quiz = quiz
        self.move_on = None

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(column=1, row=0, padx=20, pady=10)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     font=("Arial", 13, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30, padx=20)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2)

        self.canvas.itemconfig(self.question_text, text=self.next_question())

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR, text=question_text)
            self.true_button.config(state="active")
            self.false_button.config(state="active")
            return question_text
        else:
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR,
                                   text=f"End of Quiz! Total Score: {self.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_on = self.window.after(2000, self.next_question)

        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.move_on = self.window.after(2000, self.next_question)

    def check_answer_false(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_on = self.window.after(2000, self.next_question)

        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.move_on = self.window.after(2000, self.next_question)
