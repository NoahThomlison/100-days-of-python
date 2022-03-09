#Step 1 
from operator import truediv
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list)-1)]
display = []
for letter in chosen_word:
  display.append("_")

print (display)




#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter_guess = input("What letter do you want to guess? ")
index = 0

for letter in chosen_word:
  if(letter == letter_guess):
    display[index] = letter
    print (display)
  index += 1



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# win_flag = False
# for letter in chosen_word:
#   if(letter == letter_guess):
#     win_flag = True

# if win_flag == True:
#   print("you win")
# else:
#   print("you lose")
