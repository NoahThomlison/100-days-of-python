BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from numpy import e
import pandas
import random

try:
  unknown_words = pandas.read_csv("data/unknown_words.csv")
  wordsDict = {row["French"]: row["English"] for (index, row) in unknown_words.iterrows()}

except FileNotFoundError:
  words = pandas.read_csv("data/french_words.csv")
  wordsDict = {row["French"]: row["English"] for (index, row) in words.iterrows()}

frenchWord, englishWord = random.choice(list(wordsDict.items()))
print(wordsDict)
# Flip card
def flipCard():
  print("flip")
  global englishWord
  global frenchWord
  canvas.itemconfig(card_background, image=cardBack)
  canvas.itemconfig(card_word, text=englishWord)
  canvas.itemconfig(card_title, text="English")

# Change Word
def changeWord():
  global englishWord
  global frenchWord
  frenchWord, englishWord = random.choice(list(wordsDict.items()))
  canvas.itemconfig(card_word, text=frenchWord)
  canvas.itemconfig(card_title, text="French")
  canvas.itemconfig(card_background, image=cardFront)
  window.after(3000, func=flipCard)

# Correct Word
def correctWord():
  window.after_cancel(timer)
  global frenchWord
  global englishWord
  global wordsDict
  del wordsDict[frenchWord]
  data = pandas.DataFrame(wordsDict.items(), columns=['French', 'English'])
  data.to_csv("data/unknown_words.csv", index=False)
  changeWord()

# Create UI
window = Tk()
rightImage = PhotoImage(file="images/right.png")
wrongImage = PhotoImage(file="images/wrong.png")
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
window.title("Flashy")
window.config(padx=50, pady=50, width=1000, height=800, bg=BACKGROUND_COLOR)

canvas = Canvas( bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=cardFront)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=frenchWord, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
check_button = Button(image=rightImage, highlightthickness=0, command=correctWord)
check_button.grid(row=2, column=0)
x_button = Button(image=wrongImage, highlightthickness=0, command=changeWord)
x_button.grid(row=2, column=1)

timer = window.after(3000, func=flipCard)

window.mainloop()
