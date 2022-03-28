from tkinter import *
from tkinter import messagebox
from fileinput import filename

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
  website = websiteField.get()
  password = passwordField.get()
  email = emailUserNameField.get()
  if(len(email) == 0):
    messagebox.showerror(title="Error", message=f"The email cannot be blank")

  elif(len(website) == 0):
    messagebox.showerror(title="Error", message=f"The website cannot be blank")

  elif(len(password) == 0):
    messagebox.showerror(title="Error", message=f"The password cannot be blank")

  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
    if is_ok:
      with open("passwords.txt", "w") as file:
        file.write((f"{website} | {email} | {password}\n"))
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

passwordButton = Button(text="Generate Password")
passwordButton.grid(row=3,column=2)
addButton = Button(text="Add", width=36, command=savePassword)
addButton.grid(row=4,column=1, columnspan=2)

window.mainloop()
