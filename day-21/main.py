from threading import currentThread
from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from score import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

playerOne = Paddle("right")
playerTwo = Paddle("left")
gameBall = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=playerOne.go_up)
screen.onkey(key="Down", fun=playerOne.go_down)
screen.onkey(key="w", fun=playerTwo.go_up)
screen.onkey(key="s", fun=playerTwo.go_down)

game_is_on = True
while game_is_on:
  screen.update()
  gameBall.move_forward()
  gameBall.checkImpactWithWalls()
  gameBall.checkImpactWithPaddle(playerOne)
  gameBall.checkImpactWithPaddle(playerTwo)
  point = gameBall.checkIfMissed()
  if(point == "L"):
    score.l_point()
    point = ""
    gameBall.reset_position()

  elif(point == "R"):
    score.r_point()
    point = ""
    gameBall.reset_position()

screen.exitonclick()
