BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
words = pandas.read_csv("data/french_words.csv")
wordsDict = {row["French"]: row["English"] for (index, row) in words.iterrows()}

# Change Word
def changeWord():
  englishWord, frenchWord = random.choice(list(wordsDict.items()))
  canvas.itemconfig(card_word, text=frenchWord)
  canvas.itemconfig(card_title, text="French")

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
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
check_button = Button(image=rightImage, highlightthickness=0, command=changeWord)
check_button.grid(row=2, column=0)
x_button = Button(image=wrongImage, highlightthickness=0, command=changeWord)
x_button.grid(row=2, column=1)

window.mainloop()

