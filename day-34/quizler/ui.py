THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
  def __init__(self, quizBrain: QuizBrain):
    self.quiz = quizBrain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20)
    self.window.configure(bg=THEME_COLOR)

    self.canvas = Canvas(height=250, width=300)
    self.canvas.grid(row=1, column=1)
    self.imageTrue = PhotoImage(file="./images/true.png")
    self.imageFalse = PhotoImage(file="./images/false.png")

    self.scoreLabel = Label(text=f"Score:", bg=THEME_COLOR, fg='#fff')
    self.scoreLabel.grid(row=0, column=2)

    self.questionLabel = Label(text="test", font=("Arial", 20, "italic"), wraplength=250)
    self.questionLabel.grid(row=1, column=1)

    self.trueButton = Button(image = self.imageTrue, command=self.trueClick)
    self.falseButton = Button(image = self.imageFalse, command=self.falseClick)
    self.trueButton.grid(row=2, column=0, pady=(20, 10))
    self.falseButton.grid(row=2, column=2, pady=(20, 10))

    self.getNextQuestion()

    self.window.mainloop()

  def getNextQuestion(self):
    if self.quiz.still_has_questions():
      questionText = self.quiz.next_question()
      self.canvas.config(bg="white")
      self.scoreLabel.config(text=f"Score: {self.quiz.score}")
      self.questionLabel.config(text = questionText)
    else:
      self.questionLabel.config(text="End of quiz")


  def trueClick(self):
    self.giveFeedback(self.quiz.check_answer("True"))

  def falseClick(self):
    self.giveFeedback(self.quiz.check_answer("False"))

  def giveFeedback(self, isRight):
    if isRight:
      self.canvas.config(bg="green")
    else: 
      self.canvas.config(bg="red")
    self.window.after(1000, self.getNextQuestion)
