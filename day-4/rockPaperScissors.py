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
playerMove = int(input("Rock (1), Paper (2), or Scissors (3)?"))
computerMove = random.randint(1, 3)

print("Your Move:")
if playerMove == 1:
  print(f"{rock}")
elif playerMove == 2:
  print(f"{paper}")
elif playerMove == 3:
  print(f"{scissors}")

print("Computer Move:")
if computerMove == 1:
  print(f"{rock}")
elif computerMove == 2:
  print(f"{paper}")
elif computerMove == 3:
  print(f"{scissors}")
  
if((playerMove == 1 and computerMove == 2) or (playerMove == 2 and computerMove == 3) or (playerMove == 3 and computerMove == 1)):
  print("You loose")
elif((playerMove == 3 and computerMove == 2) or (playerMove == 2 and computerMove == 1) or (playerMove == 1 and computerMove == 3)):
  print("You win")
else:
  print("Tie game")