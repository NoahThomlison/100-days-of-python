from operator import truediv
from pickle import TRUE
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet?", prompt="Who will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = TRUE
turtles = []
x = -230
y = 100
for color in colors:
  print(y)
  print(color)
  turtleName = color + "turtle"
  turtleName = Turtle(shape="turtle")
  turtleName.penup()
  turtleName.color(color)
  turtleName.goto(x, y)
  y -= 40
  turtles.append(turtleName)

print(turtles)

while (is_race_on):
  for turtle in turtles:
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
    print(turtle.xcor())
    if(turtle.xcor() >= 230):
      is_race_on = False
      winningTurtle = (turtle.pencolor())
      if(winningTurtle == user_bet):
        print(f"You won! The {winningTurtle} won!")
      else:
        print(f"You lose, the winning turtle was {winningTurtle}")
        
screen.exitonclick()