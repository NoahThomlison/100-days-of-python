BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

# Create UI
window = Tk()
rightImage = PhotoImage(file="images/right.png")
wrongImage = PhotoImage(file="images/wrong.png")
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
window.title("Flashy")
window.config(padx=50, pady=50, width=1000, height=800, bg=BACKGROUND_COLOR)
background_image=PhotoImage(cardFront)
canvas = Canvas( bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
canvas.place(x=0, y=0)

check_button = Button(image=rightImage, highlightthickness=0)
check_button.place(x=600, y=600)
x_button = Button(image=wrongImage, highlightthickness=0)
x_button.place(x=200, y=600)

cardFrontLabel = Label(width=800, height=526, image=cardBack, highlightthickness=0, bg=BACKGROUND_COLOR)
cardFrontLabel.place(x=50, y=50)

cardLabel = Label(text="French", highlightthickness=0, font=("Ariel", 40, "italic"), bg=BACKGROUND_COLOR, anchor="center")
cardWord = Label(text="Trouve", font=("Ariel", 60, "bold"), bg=BACKGROUND_COLOR, anchor="center")
cardLabel.place(x=375, y=150)
cardWord.place(x=325, y=263)



window.mainloop()
