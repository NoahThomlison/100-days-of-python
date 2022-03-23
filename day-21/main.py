from threading import currentThread
from turtle import Turtle, Screen
import random
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()

playerOne = Paddle("right")
playerTwo = Paddle("left")

print(playerOne)

screen.onkey(key="Up", fun=playerOne.go_up)
screen.onkey(key="Down", fun=playerOne.go_down)

screen.exitonclick()
