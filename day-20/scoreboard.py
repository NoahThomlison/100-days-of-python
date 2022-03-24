from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    with open("data.txt") as file:
      self.high_score = file.read()
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    with open("data.txt", mode="w") as file:
      file.write(self.high_score)
    
  def reset(self):
    print(self.score)
    print(self.high_score)

    if int(self.score) > int(self.high_score):
        self.high_score = str(self.score)
    self.score = 0
    self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()
