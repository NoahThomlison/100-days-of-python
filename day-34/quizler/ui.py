THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface():
  def __init__(self):
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

    self.questionLabel = Label(text="test", font=("Arial", 20, "italic"))
    self.questionLabel.grid(row=1, column=1)

    self.trueButton = Button(image = self.imageTrue)
    self.falseButton = Button(image = self.imageFalse)
    self.trueButton.grid(row=2, column=0, pady=(20, 10))
    self.falseButton.grid(row=2, column=2, pady=(20, 10))

    self.window.mainloop()