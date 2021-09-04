from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        true_img = PhotoImage(file="Day 34 - Quizzler\\images\\true.png")
        false_img = PhotoImage(file="Day 34 - Quizzler\\images\\false.png")

        self.button_true = Button(image=true_img,
                                  bg=THEME_COLOR,
                                  borderwidth=0,
                                  relief="flat",
                                  padx=30,
                                  pady=30, command=self.check_answer)

        self.button_false = Button(image=false_img,
                                   bg=THEME_COLOR,
                                   borderwidth=0,
                                   relief="flat",
                                   padx=30,
                                   pady=30, command=self.false_button_check)

        self.canvas = Canvas(
            width=300,
            height=250,
            highlightthickness=0,
            background="white",
        )
        self.score_text = Label(text="Score: 0",
                                fg="white",
                                bg=THEME_COLOR,
                                font=("SF Compact Display", 14))

        self.title_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="The quiestion text will be here.",
            font=("SF Pro Display", 16, "italic"))

        self.score_text.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()
        

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.button_true.config(state="normal")
            self.button_false.config(state="normal")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.title_text, text=question)
        else:
            self.canvas.itemconfig(self.title_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            
    def false_button_check(self):
        self.check_answer(False)
        
    def check_answer(self, answer=True):
        result = self.quiz.check_answer(answer)
        if result == True:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            is_right = True
        else:
            is_right = False
        self.feedback(is_right)
        self.get_next_question()
        
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")
        self.window.update()
        self.window.after(1000)
