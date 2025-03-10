from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label=Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column =1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width= 280 ,text="",fill = THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.green_tick = PhotoImage(file="images/true.png")
        self.true_button=Button(image=self.green_tick, command=self.true_selected)
        self.true_button.grid(column=0, row=3)

        self.red_cross = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.red_cross, highlightthickness=0, command=self.false_selected)
        self.false_button.grid(column=1, row=3)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text, fill = THEME_COLOR, font=("Arial", 20, "italic"))
        else:
            self.canvas.itemconfig(self.text, text="That's all folks!!", fill = THEME_COLOR, font=("Arial", 20, "italic"))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_selected(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_selected(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)






