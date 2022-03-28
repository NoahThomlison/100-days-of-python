from tkinter import *
from turtle import width

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image = logo)
canvas.grid(row=0,column=1)

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1,column=0)
emailUserNameLabel = Label(text="Email/Username:")
emailUserNameLabel.grid(row=2,column=0)
passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3,column=0)

websiteField = Entry(width=35)
websiteField.grid(row=1,column=1, columnspan=2)
websiteField.focus()
emailUserNameField = Entry(width=35)
emailUserNameField.insert(0, "noahthomlison@gmail.com")
emailUserNameField.grid(row=2,column=1, columnspan=2) 

passwordField = Entry(width=21)
passwordField.grid(row=3,column=1)

passwordButton = Button(text="Generate Password")
passwordButton.grid(row=3,column=2)
addButton = Button(text="Add", width=36)
addButton.grid(row=4,column=1, columnspan=2)

window.mainloop()
