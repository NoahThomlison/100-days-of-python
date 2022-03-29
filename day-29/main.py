from tkinter import *
from tkinter import messagebox
from fileinput import filename
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def createPassword():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',   'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)
  password = "".join(password_list)
  passwordField.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
  website = websiteField.get()
  password = passwordField.get()
  email = emailUserNameField.get()
  newEntry = {
    website: {
      "email": email,
      "password": password
    }
  }
  if(len(email) == 0):
    messagebox.showerror(title="Error", message=f"The email cannot be blank")

  elif(len(website) == 0):
    messagebox.showerror(title="Error", message=f"The website cannot be blank")

  elif(len(password) == 0):
    messagebox.showerror(title="Error", message=f"The password cannot be blank")

  else:
    try:
      with open("passwords.json", "r") as file:
        oldPasswords = json.load(file)
        
    except FileNotFoundError:
      with open("passwords.json", "w") as file:
        json.dump(newEntry, file, indent=4)
        oldPasswords = json.load(file)

    else:
      oldPasswords.update(newEntry)
      with open("passwords.json", "w") as file:
        json.dump(oldPasswords, file, indent=4)
    finally:
      websiteField.delete(0, END)
      passwordField.delete(0, END)

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

passwordButton = Button(text="Generate Password", command=createPassword)
passwordButton.grid(row=3,column=2)
addButton = Button(text="Add", width=36, command=savePassword)
addButton.grid(row=4,column=1, columnspan=2)

window.mainloop()
