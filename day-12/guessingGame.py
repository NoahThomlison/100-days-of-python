#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random


print("Welcome to the guessing game!")
difficultyLevel = input("Would you like easy or hard mode?" )
difficultyLevel = difficultyLevel.lower()
if(difficultyLevel == "easy"):
  lives = 10
elif(difficultyLevel == "hard"):
  lives = 5

number = random.ranint(1, 100)
correct = False



while lives > 0 or correct == False:
  guess = int(input("What is your guess? "))
  if(guess > number):
    print("Your guess was too high.")
    lives -= 1
  elif(guess < number):
    print("Your guess was too low.")
    lives -= 1
  elif(guess == number):
    print("Your guess was correct! You win!")
    correct = True
  elif(lives == 0):
    print("You are out of lives. You loose!")
    