from multiprocessing.connection import wait


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("You're at a cross road. Where to do you want to go? Type 'left' or 'right'. ")

if direction.lower() == "left":
  waitOrSwim = input("You come to a lake. There is an island in the middle of the lake. Type `wait` to wait for a boat. Type `swim` to swim accross. ")
  if waitOrSwim.lower() == "wait":
    door = input("There is some doors, which do you choose? Red, Yellow or Blue. ")
    if door.lower() == "red":
      print("You are burned by fire. Game over")
    elif door.lower() == "yellow":
      print("You win")
    elif door.lower() == "blue":
      print("You are eaten by beasts. Game over")
    else:
      print("Game Over")z
  else:
    print("You get attacked by trout. Game over")
else:
  print("You fall into a hole. Game over")