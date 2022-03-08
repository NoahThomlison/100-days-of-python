rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
playerMove = int(input("Rock (0), Paper (1), or Scissors (2)?"))
computerMove = random.randint(0, 2)
options = [rock, paper, scissors]

print("Your Move:")
if playerMove == 0:
  print(f"{options[0]}")
elif playerMove == 1:
  print(f"{options[1]}")
elif playerMove == 2:
  print(f"{options[2]}")

print("Computer Move:")
if computerMove == 0:
  print(f"{options[0]}")
elif computerMove == 1:
  print(f"{options[1]}")
elif computerMove == 2:
  print(f"{options[2]}")
  
if((playerMove == 0 and computerMove == 1) or (playerMove == 1 and computerMove == 2) or (playerMove == 2 and computerMove == 0)):
  print("You loose")
elif((playerMove == 2 and computerMove == 1) or (playerMove == 1 and computerMove == 0) or (playerMove == 0 and computerMove == 2)):
  print("You win")
else:
  print("Tie game")