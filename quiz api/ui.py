from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("QUIZ")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR,highlightthickness=0)
        # self.create_button()

        self.right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_img, highlightthickness=0,width=90,height=90,command=self.True_answer)
        self.right.grid(row=2, column=0)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_img, highlightthickness=0,width=90,height=90,command=self.False_answer)
        self.wrong.grid(row=2, column=1)
        self.label=Label(text="SCORE",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)





    # def create_canvas(self):
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)

        self.question_text = self.canvas.create_text(150, 120, text="HELLO",fill=THEME_COLOR,font=("Arial",20,"italic"),width=290)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        self.get_next_question()


        self.window.mainloop()

    def True_answer(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def False_answer(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the Quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
        # self.answer=

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

    # def create_button(self):
    #     right_img = PhotoImage(file="images/true.png")
    #     right = Button(image=right_img, highlightthickness=0)
    #     right.grid(row=2, column=1)
    #
    #     wrong_img = PhotoImage(file="images/false.png")
    #     wrong = Button(image=wrong_img, highlightthickness=0)
    #     wrong.grid(row=2, column=0)
