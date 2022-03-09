#Step 1 
from operator import truediv
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = word_list[random.randint(0, len(word_list)-1)]
display = []
for letter in chosen_word:
  display.append("_")

print (display)
guessFlag = False

while "_" in display and lives >= 0:
  index = 0
  guessFlag = False
  letter_guess = input("What letter do you want to guess? ")
  for letter in chosen_word:
    if(letter == letter_guess):
      display[index] = letter
      guessFlag = True
    index += 1
  if guessFlag == False:
    print(stages[lives])
    print (display)
    lives -= 1
  else:
    print(stages[lives])
    print (display)

if(lives >= 0):
  print("You win!")
else:
  print("You lose!")