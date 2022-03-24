from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Frogger")
screen.tracer(0)

frogger = Player()
game_on = True
numOfCars = 30
cars = []


for x in range(0, numOfCars):
  car = Car()
  cars.append(car)

screen.listen()
screen.onkey(key="w", fun=frogger.move_forward)
screen.onkey(key="a", fun=frogger.move_left)
screen.onkey(key="s", fun=frogger.move_back)
screen.onkey(key="d", fun=frogger.move_right)

x = 0
while game_on:
  screen.update()
  time.sleep(0.05)
  for car in cars:
    car.move_forward()
    if(car.check_impact(frogger) or frogger.check_at_finish_line()):
      game_on = False
    if(car.is_off_screen()):
      cars.remove(car)
      car = Car()
      cars.append(car)
  print(x)

print(cars)
screen.exitonclick()
