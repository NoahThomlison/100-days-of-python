from os import stat
from re import S
from turtle import Screen, Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 

correctCount = 0
state_data = pandas.read_csv("50_states.csv")
gameOn = True

while gameOn:
  correct_states = []
  answer = screen.textinput(title="Guess a state", prompt=f"What is a state name? {correctCount}/50").title()
  states = list(state_data.state)

  if answer in states:
    x = int(state_data[state_data['state']==answer]['x'])
    y = int(state_data[state_data['state']==answer]['y'])
    answer_turtle = Turtle()
    answer_turtle.hideturtle()
    answer_turtle.penup()
    answer_turtle.goto(x, y)
    answer_turtle.write(answer)
    correctCount += 1
    correct_states.append(answer)
  if(correctCount == 50 or answer == "Exit"):
    gameOn = False
    missing_states = []
    for state in states:
      if state not in correct_states:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("Missing States")